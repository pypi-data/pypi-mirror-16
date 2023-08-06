###############################################################################
#       Copyright (C) 2011-2012 Burcin Erocal <burcin@erocal.org>
#                     2016      Vincent Delecroix <vincent.delecroix@labri.fr>
#  Distributed under the terms of the GNU General Public License (GPL),
#  version 3 or any later version.  The full text of the GPL is available at:
#                  http://www.gnu.org/licenses/
###############################################################################

from libcpp cimport bool
from libcpp.string cimport string
from cygmp.types cimport mpz_t, mpq_t, mpz_srcptr

cdef extern from "wrap.h" namespace "polymake":
    pass

cdef extern from "polymake/Main.h" namespace "polymake":
    cdef cppclass Main:
        void set_application(char*)
        void set_preference(char*)

cdef extern from "polymake/Integer.h" namespace 'polymake':
    ctypedef pm_const_Integer "const Integer"
    cdef cppclass pm_Integer "Integer" :
        mpz_t get_rep()
        pm_Integer set_mpz "set" (mpz_t)
        Py_ssize_t strsize(int)
        int compare(int)
        long to_long()   # FIXME: this is const
        double to_double()
        pm_Integer& set(mpz_srcptr)

        bool non_zero()

        bool operator== (pm_Integer)
        bool operator== (long)
        bool operator> (pm_Integer)
        bool operator> (long)
        bool operator< (pm_Integer)
        bool operator< (long)

        int compare(pm_Integer)
        int compare(long)

        pm_Integer operator+ (pm_Integer)
        pm_Integer operator+ (long)
        pm_Integer operator- ()
        pm_Integer operator- (pm_Integer)
        pm_Integer operator- (long)
        pm_Integer operator* (pm_Integer)
        pm_Integer operator* (long)
        pm_Integer operator/ (pm_Integer)
        pm_Integer operator/ (long)
        pm_Integer negate()

cdef extern from "polymake/Rational.h" namespace 'polymake':
    ctypedef pm_const_Rational "const Rational"
    cdef cppclass pm_Rational "Rational":
        mpq_t get_rep()
        pm_Rational set_mpq_t "set" (mpq_t)
        pm_Rational& set_mpq_srcptr "set" (mpq_srcptr)

        pm_Rational abs()

        bool non_zero()

        bool operator== (pm_Rational)
        bool operator== (pm_Integer)
        bool operator== (long)
        bool operator< (pm_Rational)
        bool operator< (pm_Integer)
        bool operator< (long)
        bool operator> (pm_Rational)
        bool operator> (pm_Integer)
        bool operator> (long)

        int compare(pm_Rational)
        int compare(pm_Integer)
        int compare(long)

        pm_Rational operator+ (pm_Rational)
        pm_Rational operator+ (pm_Integer)
        pm_Rational operator+ (long)
        pm_Rational operator- ()
        pm_Rational operator- (pm_Rational)
        pm_Rational operator- (pm_Integer)
        pm_Rational operator- (long)
        pm_Rational operator* (pm_Rational)
        pm_Rational operator* (pm_Integer)
        pm_Rational operator* (long)
        pm_Rational operator/ (pm_Rational)
        pm_Rational operator/ (pm_Integer)
        pm_Rational operator/ (long)


cdef extern from "polymake/client.h":
    cdef cppclass pm_PerlPropertyValue "perl::PropertyValue":
        pass

    cdef cppclass pm_PerlObject "perl::Object":
        pm_PerlObject()
        pm_PerlObject(char*) except +ValueError
        bool valid()
        void VoidCallPolymakeMethod(char*) except +ValueError
        void save(char*)
        pm_PerlPropertyValue take(char*)
        pm_PerlPropertyValue give(char*) # do not add except here, see pm_get for why
        pm_PerlObjectType type()
        int exists(const string& name)
        string name()
        string description()
        bool isa(pm_PerlObjectType)
        pm_PerlObject parent()

    cdef cppclass pm_PerlObjectType "perl::ObjectType":
        string name()

    pm_PerlObject CallPolymakeFunction (char*) except +ValueError
    pm_PerlObject CallPolymakeFunction1 "CallPolymakeFunction" \
            (char*, int) except +ValueError
    pm_PerlObject CallPolymakeFunction2 "CallPolymakeFunction" \
            (char*, int, int) except +ValueError
    pm_PerlObject CallPolymakeFunction3 "CallPolymakeFunction" \
            (char*, int, int, int) except +ValueError
    pm_PerlObject* new_PerlObject_from_PerlObject "new perl::Object" (pm_PerlObject)


cdef extern from "polymake/Matrix.h" namespace 'polymake':
    cdef cppclass pm_MatrixRational "Matrix<Rational>":
        pm_MatrixRational()
        pm_MatrixRational(int nr, int nc)
        void assign(int r, int c, pm_Rational val)
        pm_MatrixRational operator|(pm_MatrixRational)
        Py_ssize_t rows()
        Py_ssize_t cols()

    # WRAP_CALL(t,i,j) -> t(i,j)
    pm_Rational get_element "WRAP_CALL"(pm_MatrixRational, int i, int j)

#cdef extern from "polymake/GenericVector.h" namespace 'polymake':
    pm_MatrixRational ones_vector_Rational "ones_vector<Rational>" ()

#cdef extern from "polymake/GenericMatrix.h" namespace 'polymake':
    pm_MatrixRational unit_matrix_Rational "unit_matrix<Rational>" (int dim)


    # WRAP_OUT(x,y) x<<y
    void pm_assign_MatrixRational "WRAP_OUT" (pm_PerlPropertyValue, pm_MatrixRational)

    # the except clause below is fake
    # it is used to catch errors in PerlObject.give(), however adding
    # the except statement to the declaration of give() makes cython
    # split lines like
    #        pm_get(self.pm_obj.give(prop), pm_res)
    # and store the result of give() first. This causes problems since
    # pm_PerlPropertyValue doesn't have a default constructor.

    # WRAP_IN(x,y) x>>y
    void pm_get_Integer "WRAP_IN" (pm_PerlPropertyValue, pm_Integer) except +ValueError
    void pm_get_Rational "WRAP_IN" (pm_PerlPropertyValue, pm_Rational) except +ValueError
    void pm_get_MatrixRational "WRAP_IN" (pm_PerlPropertyValue, pm_MatrixRational) except +ValueError
    void pm_get_VectorInteger "WRAP_IN" (pm_PerlPropertyValue, pm_VectorInteger) except +ValueError
    void pm_get_PerlObject "WRAP_IN" (pm_PerlPropertyValue, pm_PerlObject) except +ValueError

cdef extern from "polymake/Vector.h" namespace 'polymake':
    cdef cppclass pm_VectorInteger "Vector<Integer>":
        pm_VectorInteger()
        pm_VectorInteger(int nr)
        #void assign(int r, int val)
        pm_Integer get "operator[]" (int i)
        int size()

    cdef cppclass pm_VectorRational "Vector<Rational>":
        pm_VectorRational()
        pm_VectorRational(int nr)
        pm_Rational get "operator []" (int i)
        int size()
