def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    #a = (S-d*d)/(2*d)
    #b = (S-d*d)/(2*d) + d
    return (S-d*d)/(2*d) + d -(((S-d*d)/(2*d)**2)/(2*(S-d*d)/(2*d) + d))
print(main(16,4))
