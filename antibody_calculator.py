while True:

    final_volume=float(raw_input('Enter Final volume:'))
    start_fold=float(raw_input('Enter concentrate fold:'))

    if final_volume>=0 and start_fold>1:
        concentration=final_volume/start_fold
        dilute_solution=final_volume-concentration
        print 'Adding ' +str("%.4f" % concentration)+" "+ str(start_fold)+\
              'x concentrate ' \
              +'in '+str("%.4f" % dilute_solution)+' dilute solution!!'
    else:
        print 'Keying value is wrong!!'
