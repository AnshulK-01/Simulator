import csv
import os
# ...existing code...

def simulationTime():
    global timeElapsed, simTime
    while(True):
        timeElapsed += 1
        time.sleep(0.66)
        if(timeElapsed==simTime):
            totalVehicles = 0
            print('Lane-wise Vehicle Counts')
            for i in range(noOfSignals):
                print('Lane',i+1,':',vehicles[directionNumbers[i]]['crossed'])
                totalVehicles += vehicles[directionNumbers[i]]['crossed']
            print('Total vehicles passed: ',totalVehicles)
            print('Total time passed: ',timeElapsed)
            print('No. of vehicles passed per unit time: ',(float(totalVehicles)/float(timeElapsed)))
            
            # --- Save result to CSV ---
            result_path = 'Charts/static_results.csv'
            write_header = not os.path.exists(result_path)
            with open(result_path, 'a', newline='') as f:
                writer = csv.writer(f)
                if write_header:
                    writer.writerow(['No.', 'Static'])
                # Find next attempt number
                try:
                    import pandas as pd
                    df = pd.read_csv(result_path)
                    attempt_no = len(df) + 1
                except:
                    attempt_no = 1
                writer.writerow([attempt_no, totalVehicles])
            # --- End CSV save ---
            
            os._exit(1)