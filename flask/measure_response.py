import requests
import time
import numpy as np
from tqdm import tqdm

if __name__ == "__main__":
    # Example loan application
    application ={
        ' Flow Duration': 94902.0,
         ' Total Fwd Packets': 1.0,
         'Total Length of Fwd Packets': 0.0,
         ' Fwd Packet Length Max': 0.0,
         ' Fwd Packet Length Min': 0.0,
         ' Fwd Packet Length Mean': 0.0,
         'Bwd Packet Length Max': 0.0,
         ' Bwd Packet Length Min': 0.0,
         'Flow Bytes/s': 0.0,
         ' Flow Packets/s': 21.07437146,
         ' Flow IAT Mean': 94902.0,
         ' Flow IAT Std': 0.0,
         ' Flow IAT Min': 94902.0,
         ' Fwd IAT Mean': 0.0,
         ' Fwd IAT Std': 0.0,
         ' Fwd IAT Min': 0.0,
         'Bwd IAT Total': 0.0,
         ' Bwd IAT Mean': 0.0,
         ' Bwd IAT Std': 0.0,
         ' Bwd IAT Max': 0.0,
         ' Bwd IAT Min': 0.0,
         'Fwd PSH Flags': 0.0,
         ' Fwd URG Flags': 0.0,
         ' Fwd Header Length': 32.0,
         'Fwd Packets/s': 10.537186,
         ' Bwd Packets/s': 10.537186,
         ' Min Packet Length': 0.0,
         ' Packet Length Variance': 0.0,
         'FIN Flag Count': 0.0,
         ' RST Flag Count': 0.0,
         ' PSH Flag Count': 0.0,
         ' ACK Flag Count': 1.0,
         ' URG Flag Count': 1.0,
         ' Down/Up Ratio': 1.0,
         'Init_Win_bytes_forward': 304.0,
         ' Init_Win_bytes_backward': 254.0,
         ' act_data_pkt_fwd': 0.0,
         'Active Mean': 0.0,
         ' Active Std': 0.0,
         ' Active Max': 0.0,
         ' Active Min': 0.0,
         ' Idle Std': 0.0}

    # Location of my server
    url = "http://0.0.0.0:8989/predict"
    
    resp = requests. post(url, json=application)
    print(resp.json())

    # Measure the response time
    all_times = []
    # For 1000 times
    for i in tqdm(range(1000)):
        t0 = time.time_ns() // 1_000_000
        # Send a request
        resp = requests.post(url, json=application)
        t1 = time.time_ns() // 1_000_000
        # Measure how much time it took to get a response in ms
        time_taken = t1 - t0
        all_times.append(time_taken)

    # Print out the results
    print("Response time in ms:")
    print("Median:", np.quantile(all_times, 0.5))
    print("95th precentile:", np.quantile(all_times, 0.95))
    print("Max:", np.max(all_times))
