"""
    This module contains the parsing parts for the c3 language
"""

import logging
from ...common import CompilerError
from .astnodes import Member, Literal, TypeCast, Unop, Binop
from .astnodes import Assignment, ExpressionStatement, Compound
from .astnodes import Return, While, If, Empty, For
from .astnodes import FunctionType, Function, FormalParameter
from .astnodes import StructureType, DefinedType, PointerType, ArrayType
from .astnodes import Constant, Variable, Sizeof
from .astnodes import StructField, Deref, Index
from .astnodes import Identifier, FunctionCall
from .scope import Scope


class Parser:
    """ Parses sourcecode into an abstract syntax tree (AST) """
    def __init__(self, diag):
        self.logger = logging.getLogger('c3')
        self.diag = diag
        self.current_scope = None
        self.token = None
        self.tokens = None
        self.mod = None

    def init_lexer(self, tokens):
        self.tokens = tokens
        self.token = self.tokens.__next__()

    def parse_source(self, tokens, context):
        """ Parse a module from tokens """
        self.logger.debug('Parsing source')
        self.init_lexer(tokens)
        try:
            module = self.parse_module(context)
            self.logger.debug('Parsing complete')
        except CompilerError as ex:
            self.diag.add_diag(ex)
            raise
        return module

    def error(self, msg, loc=None):
        """ Raise an error at the current location """
        if loc is None:
            loc = self.token.loc
        raise CompilerError(msg, loc)

    # Lexer helpers:
    def consume(self, typ=None):
        """ Assert that the next token is typ, and if so, return it. If
            typ is not given, consume the next token.
        """
        if typ is None:
            typ = self.peak
        if self.peak == typ:
            return self.next_token()
        else:
            self.error('Excected: "{0}", got "{1}"'.format(typ, self.peak))

    @property
    def peak(self):
        """ Look at the next token to parse without popping it """
        return self.token.typ

    def has_consumed(self, typ):
        """ Checks if the look-ahead token is of type typ, and if so
            eats the token and returns true """
        if self.peak == typ:
            self.consume()
            return True
        return False

    def next_token(self):
        """ Advance to the next token """
        tok = self.token
        if tok.typ != 'EOF':
            self.token = self.tokens.__next__()
        return tok

    def add_symbol(self, sym):
        """ Add a symbol to the current scope """
        if self.current_scope.has_symbol(sym.name, include_parent=False):
            self.error('Redefinition of {0}'.format(sym.name), loc=sym.loc)
        else:
            self.current_scope.add_symbol(sym)

    def parse_module(self, context):
        """ Parse a module definition """
        self.consume('module')
        name = self.consume('ID')
        self.consume(';')
        self.logger.debug('Parsing package %s', name.val)
        self.mod = context.get_module(name.val)
        self.current_scope = self.mod.inner_scope
        while self.peak != 'EOF':
            self.parse_top_level()
        self.consume('EOF')
        return self.mod

    def parse_top_level(self):
        """ Parse toplevel declaration """
        # Handle public specifier:
        public = self.has_consumed('public')

        # Handle a toplevel construct
        if self.peak == 'function':
            self.parse_function_def(public=public)
        elif self.peak == 'var':
            self.parse_variable_def()
        elif self.peak == 'const':
            self.parse_const_def()
        elif self.peak == 'type':
            self.parse_type_def(public=public)
        elif self.peak == 'import' and not public:
            self.parse_import()
        else:
            self.error('Expected function, var, const or type')

    def parse_import(self):
        """ Parse import construct """
        self.consume('import')
        name = self.consume('ID').val
        self.mod.imports.append(name)
        self.consume(';')

    def parse_designator(self):
        """ A designator designates an object with a name. """
        name = self.consume('ID')
        return Identifier(name.val, self.current_scope, name.loc)

    def parse_id_sequence(self):
        """ Parse a sequence of id's """
        ids = [self.consume('ID')]
        while self.has_consumed(','):
            ids.append(self.consume('ID'))
        return ids

    # Type system
    def parse_type_spec(self):
        """ Parse type specification. Type specs are read from right to left.

        A variable spec is given by:
        var [typeSpec] [modifiers] [pointer/array suffix] variable_name

        For example:
        var int volatile * ptr;
        creates a pointer to a volatile integer.
        """
        # Parse the first part of a type spec:
        if self.peak == 'struct':
            self.consume('struct')
            self.consume('{')
            mems = []
            while self.peak != '}':
                mem_t = self.parse_type_spec()
                for i in self.parse_id_sequence():
                    mems.append(StructField(i.val, mem_t))
                self.consume(';')
            self.consume('}')
            the_type = StructureType(mems)
        elif self.peak == 'enum':
            raise NotImplementedError('enum not yet implemented')
        else:
            # The type is identified by an identifier:
            the_type = self.parse_designator()
            while self.has_consumed('.'):
                field = self.consume('ID')
                the_type = Member(the_type, field.val, field.loc)

        # Check for the volatile modifier (this is a suffix):
        the_type.volatile = self.has_consumed('volatile')

        # Check for pointer or array suffix:
        while self.peak in ['*', '[']:
            if self.has_consumed('*'):
                the_type = PointerType(the_type)
            elif self.has_consumed('['):
                size = self.parse_expression()
                self.consume(']')
                the_type = ArrayType(the_type, size)
            else:  # pragma: no cover
                raise RuntimeError()

            # Check (again) for the volatile modifier:
            the_type.volatile = self.has_consumed('volatile')
        return the_type

    def parse_type_def(self, public=True):
        """ Parse a type definition """
        self.consume('type')
        newtype = self.parse_type_spec()
        typename = self.consume('ID')
        self.consume(';')
        typedef = DefinedType(typename.val, newtype, public, typename.loc)
        self.add_symbol(typedef)

    def parse_variable_def(self, allow_init=False, public=True):
        """ Parse variable declaration, optionally with initialization. """
        self.consume('var')
        var_type = self.parse_type_spec()
        statements = []
        while True:
            name = self.consume('ID')
            var = Variable(name.val, var_type, public, name.loc)
            # Munch initial value:
            if allow_init and self.peak == '=':
                loc = self.consume('=').loc
                rhs = self.parse_expression()
                lhs = Identifier(name.val, self.current_scope, name.loc)
                statements.append(Assignment(lhs, rhs, loc, '='))
            self.add_symbol(var)
            if not self.has_consumed(','):
                break
        self.consume(';')
        if allow_init:
            return Compound(statements)

    def parse_const_def(self):
        """ Parse a constant definition """
        self.consume('const')
        typ = self.parse_type_spec()
        while True:
            name = self.consume('ID')
            self.consume('=')
            val = self.parse_expression()
            constant = Constant(name.val, typ, val, name.loc)
            self.add_symbol(constant)
            if not self.has_consumed(','):
                break
        self.consume(';')

    def parse_function_def(self, public=True):
        """ Parse function definition """
        loc = self.consume('function').loc
        returntype = self.parse_type_spec()
        fname = self.consume('ID').val
        self.logger.debug('Parsing function %s', fname)
        func = Function(fname, public, loc)
        self.add_symbol(func)
        func.inner_scope = Scope(self.current_scope)
        func.package = self.mod
        self.current_scope = func.inner_scope
        self.consume('(')
        parameters = []
        if not self.has_consumed(')'):
            while True:
                typ = self.parse_type_spec()
                name = self.consume('ID')
                param = FormalParameter(name.val, typ, name.loc)
                self.add_symbol(param)
                parameters.append(param)
                if not self.has_consumed(','):
                    break
            self.consume(')')
        paramtypes = [p.typ for p in parameters]
        func.typ = FunctionType(paramtypes, returntype)
        func.parameters = parameters
        if self.has_consumed(';'):
            func.body = None
        else:
            func.body = self.parse_compound()
        self.current_scope = self.current_scope.parent

    def parse_if(self):
        """ Parse if statement """
        loc = self.consume('if').loc
        self.consume('(')
        condition = self.parse_expression()
        self.consume(')')
        true_code = self.parse_statement()
        if self.has_consumed('else'):
            false_code = self.parse_statement()
        else:
            false_code = Empty()
        return If(condition, true_code, false_code, loc)

    def parse_while(self):
        """ Parses a while statement """
        loc = self.consume('while').loc
        self.consume('(')
        condition = self.parse_expression()
        self.consume(')')
        statements = self.parse_statement()
        return While(condition, statements, loc)

    def parse_for(self):
        """ Parse a for statement """
        loc = self.consume('for').loc
        self.consume('(')
        init = self.parse_statement()
        self.consume(';')
        condition = self.parse_expression()
        self.consume(';')
        final = self.parse_statement()
        self.consume(')')
        statements = self.parse_statement()
        return For(init, condition, final, statements, loc)

    def parse_return(self):
        """ Parse a return statement """
        loc = self.consume('return').loc
        if self.has_consumed(';'):
            return Return(None, loc)
        else:
            expr = self.parse_expression()
            self.consume(';')
            return Return(expr, loc)

    def parse_compound(self):
        """ Parse a compound statement, which is bounded by '{' and '}' """
        self.consume('{')
        statements = []
        while self.peak != '}':
            statements.append(self.parse_statement())
        self.consume('}')

        # Enforce styling:
        # if cb1.loc.col != cb2.loc.col:
        #    self.error('Braces not in same column!')

        return Compound(statements)

    def parse_statement(self):
        """ Determine statement type based on the pending token """
        if self.peak == 'if':
            return self.parse_if()
        elif self.peak == 'while':
            return self.parse_while()
        elif self.peak == 'for':
            return self.parse_for()
        elif self.peak == '{':
            return self.parse_compound()
        elif self.has_consumed(';'):
            return Empty()
        elif self.peak == 'var':
            return self.parse_variable_def(allow_init=True)
        elif self.peak == 'return':
            return self.parse_return()
        else:
            expression = self.parse_unary_expression()
            if self.peak in Assignment.operators:
                # We enter assignment mode here.
                operator = self.peak
                loc = self.consume(operator).loc
                rhs = self.parse_expression()
                return Assignment(expression, rhs, loc, operator)
            else:
                # Must be call statement!
                return ExpressionStatement(expression, expression.loc)

    LEFT_ASSOCIATIVITY = 1
    op_binding_powers = {
        'or': (10, LEFT_ASSOCIATIVITY),
        'and': (20, LEFT_ASSOCIATIVITY),
        '==': (30, LEFT_ASSOCIATIVITY), '<': (30, LEFT_ASSOCIATIVITY),
        '>': (30, LEFT_ASSOCIATIVITY), '<=': (30, LEFT_ASSOCIATIVITY),
        '>=': (30, LEFT_ASSOCIATIVITY), '!=': (30, LEFT_ASSOCIATIVITY),
        '<<': (40, LEFT_ASSOCIATIVITY), '>>': (40, LEFT_ASSOCIATIVITY),
        '+': (50, LEFT_ASSOCIATIVITY), '-': (50, LEFT_ASSOCIATIVITY),
        '*': (60, LEFT_ASSOCIATIVITY), '/': (60, LEFT_ASSOCIATIVITY),
        '%': (60, LEFT_ASSOCIATIVITY),
        '|': (70, LEFT_ASSOCIATIVITY),
        '&': (80, LEFT_ASSOCIATIVITY), '^': (80, LEFT_ASSOCIATIVITY)
    }

    def parse_expression(self, rbp=0):
        """ Process expressions with precedence climbing
            See also:
            http://eli.thegreenplace.net/2012/08/02/
                parsing-expressions-by-precedence-climbing
        """
        lhs = self.parse_cast_expression()
        while self.peak in self.op_binding_powers and \
                self.op_binding_powers[self.peak][0] >= rbp:
            operator = self.consume()
            precedence, associativity = self.op_binding_powers[operator.typ]
            if associativity == self.LEFT_ASSOCIATIVITY:
                next_precedence = precedence + 1
            else:
                next_precedence = precedence
            rhs = self.parse_expression(next_precedence)
            lhs = Binop(lhs, operator.typ, rhs, operator.loc)
        return lhs

    # Domain of unary expressions:

    def parse_cast_expression(self):
        """
          the C-style type cast conflicts with '(' expr ')'
          so introduce extra keyword 'cast'
        """
        if self.peak == 'cast':
            loc = self.consume('cast').loc
            self.consume('<')
            to_type = self.parse_type_spec()
            self.consume('>')
            self.consume('(')
            inner_expression = self.parse_expression()
            self.consume(')')
            return TypeCast(to_type, inner_expression, loc)
        elif self.peak == 'sizeof':
            # Compiler internal function to determine size of a type
            loc = self.consume('sizeof').loc
            self.consume('(')
            typ = self.parse_type_spec()
            self.consume(')')
            return Sizeof(typ, loc)
        else:
            return self.parse_unary_expression()

    def parse_unary_expression(self):
        """ Handle unary plus, minus and pointer magic """
        if self.peak in ['&', '*', '-', '+', 'not']:
            operation = self.consume()
            inner_expression = self.parse_cast_expression()
            if operation.val == '*':
                return Deref(inner_expression, operation.loc)
            else:
                return Unop(operation.typ, inner_expression, operation.loc)
        else:
            return self.parse_postfix_expression()

    def parse_postfix_expression(self):
        """ Parse postfix expression """
        pfe = self.parse_primary_expression()
        while self.peak in ['[', '.', '->', '(']:
            if self.has_consumed('['):
                i = self.parse_expression()
                self.consume(']')
                pfe = Index(pfe, i, i.loc)
            elif self.has_consumed('->'):
                field = self.consume('ID')
                pfe = Deref(pfe, pfe.loc)
                pfe = Member(pfe, field.val, field.loc)
            elif self.has_consumed('.'):
                field = self.consume('ID')
                pfe = Member(pfe, field.val, field.loc)
            elif self.has_consumed('('):
                # Function call
                args = []
                if not self.has_consumed(')'):
                    args.append(self.parse_expression())
                    while self.has_consumed(','):
                        args.append(self.parse_expression())
                    self.consume(')')
                pfe = FunctionCall(pfe, args, pfe.loc)
            else:  # pragma: no cover
                raise RuntimeError()
        return pfe

    def parse_primary_expression(self):
        """ Literal and parenthesis expression parsing """
        if self.peak == '(':
            self.consume('(')
            expr = self.parse_expression()
            self.consume(')')
        elif self.peak == 'NUMBER':
            val = self.consume('NUMBER')
            expr = Literal(val.val, val.loc)
        elif self.peak == 'REAL':
            val = self.consume('REAL')
            expr = Literal(val.val, val.loc)
        elif self.peak == 'true':
            val = self.consume('true')
            expr = Literal(True, val.loc)
        elif self.peak == 'false':
            val = self.consume('false')
            expr = Literal(False, val.loc)
        elif self.peak == 'STRING':
            val = self.consume('STRING')
            expr = Literal(val.val, val.loc)
        elif self.peak == 'ID':
            expr = self.parse_designator()
        else:
            self.error('Expected NUM, ID or (expr), got {0}'.format(self.peak))
        return expr
