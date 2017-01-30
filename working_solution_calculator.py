while True:
    
    start_fold=list()
        
    final_volume=raw_input('Enter Final volume (ul) :')
    dilute_solution=raw_input('Enter dilute solution:[or press Enter to skip]') or 'Dilute solution'
    start_fold_input=raw_input('Enter concentrate folds:[use space to split mutiple concentrate folds]')

    
    try:
        final_volume=float(final_volume)
        start_fold=start_fold_input.split()
        start_fold=[float(x) for x in start_fold]    
    except:
        print 'Wrong final volume or wrong start fold!!'


    stock_volume=list()
    stock_name=list()
    fold_count=0
    for x in start_fold:
        y=final_volume/x
        stock_volume.append(y)
        fold_count=fold_count+1
        stock_name.append('StockNo'+str(fold_count))

   
    dilute_volume=final_volume
    for y in stock_volume:
        dilute_volume=dilute_volume-y
 

    if dilute_volume<0:
        print 'Wrong start fold, can\'t add all stock into working solution!!'
    else:
        print "Adding"
        for num in range(len(start_fold)):
            print str("%.3f" % stock_volume[num]) + ' ul '\
                   +str(start_fold[num]) + 'x '+str(stock_name[num])
        print 'in ' + str("%.3f" % dilute_volume)+' '+dilute_solution
    

