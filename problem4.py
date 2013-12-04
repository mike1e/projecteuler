def largest_palindrone():
    '''
      Finds largest palindrone of 3 digit products.
    '''
    palindrone = 0
    for a in xrange(100,999):
        for b in xrange(100,999):
            product = a*b
            if product > palindrone and str(product) == str(product)[::-1]:
                palindrone = product
    print palindrone

largest_palindrone()
