
import locale
def demoFunc(format):
    try:
        ret = locale.format_string (format, 2)                                               
    except (ImportError,AttributeError,OSError,NameError,AssertionError,TypeError) as e:
        print (e)
demoFunc ("%9663511110u")                                    



