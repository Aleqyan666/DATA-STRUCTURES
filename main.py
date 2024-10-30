from .collections.Collections import LinkedListBasedStack, ArrayBasedStack, ListADT, LinkedList, ArrayBasedList


# NOTE: Stacks are commonly used to reverse collections, as whatever data you feed to it,
# you read it back in reverse order
def reverse(l: ListADT):
    # the fact that we have added the function property type, does not stop the user
    # in python to pass an object or some other type to the function
    # what it does, is hints python wich which object we'll be operating in this function
    # try to perform the "l." operation in scope of this method and you will see that the
    # IDE will hint you all public methods for ListADT class
    st = ArrayBasedStack()
    for e in l:
        st.push(e)
    print(st)
    l.clear()
    while st.top() != None:
        l.add_last(st.pop())


# NOTE: This is a skeleton recursive (non instance) static method which goes through
# all list objects recursively
def iterate_list_recursive(l:ListADT):
    if l.size() == 0:
        return
    f = l.first()
    l.remove_first()
    # If you put the print statement, or use the f value here (before rec call)
    # you will be visiting the list element in forward order
    print(f)
    double_list_elems_rec(l)
    # If you put the print statement, or use the f value here (after rec call)
    # you will be visiting the list elements in backward (reverse) order
    l.add_first(f)


def double_list_elems_rec(l: ListADT):
    if l.size() == 0:
        return
    f = l.first()
    l.remove_first()
    double_list_elems_rec(l)
    l.add_first(f)
    l.add_first(f)


def reverse_rec(l: ListADT):
    if l.size() == 0:
        return
    f = l.first()
    l.remove_first()
    reverse_rec(l)
    l.add_last(f)


l = LinkedList()
for i in range(10):
    l.add_last(i)
print(l)
reverse(l)
print(l)
double_list_elems_rec(l)
print("List after doubling  ", l)
reverse_rec(l)
print("List after reverse  ", l)

st = ArrayBasedStack()
st.push(5)
st.push(6)
st.push(10)
print(st)
print(st.top())


# NOTE: we can use stack to implement the method checking if the parenthesis are put
# correctly in an expression. Each time we meet a open brace, we add it to the stack
# and each time we meet a close brace, we remove an open brace from stack.
# In case we meet a close brace and there is no open brace in stack to remove, then the order
# of braces is invalid. If we go through the whole expression, we expect all open braces to
# have their matching closing braces, hence after full traversal of the expression, the stack
# should be empty. If that's not the case, then the order of braces is invalid.
def check_parenthesis_using_stack(exp):
    st = LinkedListBasedStack()
    for char in exp:
        if char == "(":
            st.push("(")
        if char == ")":
            if st.top():
                st.pop()
            else:
                return False
    if st.top():
        return False
    else:
        return True


print(check_parenthesis_using_stack("((()()))()(())"))
print(check_parenthesis_using_stack("()"))
