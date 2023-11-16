# DSM-Project
Into to Data Science and Mining Final Project

## Project Goal

  The goal of this project is to answer the question:
  "What trends or factors determine a DDoS attack?"

## Methods

  The primary method that makes this project successful is to use a supervised model to effectively classify the data and find the specific patterns that make up a definite attack.

  The outcome of this method should be to make a chart to visualize the data contained within the dataset to allow for a visual aid within the final poster that this project makes up.

## Dataset

  All data is gathered from [KAGGLE](https://www.kaggle.com/datasets/aymenabb/ddos-evaluation-dataset-cic-ddos2019)

# Procedure

## Preparing the data

### Initial Questions:

#### What does it look like?

  The data based off of the raw format is stored in its own CSV format and has an extra newline within the data along with spaces between the column title. We can extract the specified datatype using a Python Script to determine the datatype for us.

  The Header Column shows that the following are stored in the dataset:

|Header|Datatype|
|:-|:-:|
|Flow ID|string|
|Source IP|string|
|Source Port|integer|
|Destination IP|string|
|Destination Port|integer|
|Protocol|integer|
|Timestamp|string|
|Flow Duration|integer|
|Total Fwd Packets|integer|
|Total Backward Packets|integer|
|Total Length of Fwd Packets|integer|
|Total Length of Bwd Packets|integer|
|Fwd Packet Length Max|integer|
|Fwd Packet Length Min|integer|
|Fwd Packet Length Mean|double|
|Fwd Packet Length Std|double|
|Bwd Packet Length Max|integer|
|Bwd Packet Length Min|integer|
|Bwd Packet Length Mean|double|
|Bwd Packet Length Std|double|
|Flow Bytes/s|double|
|Flow Packets/s|double|
|Flow IAT Mean|double|
|Flow IAT Std|double|
|Flow IAT Max|integer|
|Flow IAT Min|integer|
|Fwd IAT Total|integer|
|Fwd IAT Mean|double|
|Fwd IAT Std|double|
|Fwd IAT Max|integer|
|Fwd IAT Min|integer|
|Bwd IAT Total|integer|
|Bwd IAT Mean|double|
|Bwd IAT Std|double|
|Bwd IAT Max|integer|
|Bwd IAT Min|integer|
|Fwd PSH Flags|integer|
|Bwd PSH Flags|integer|
|Fwd URG Flags|integer|
|Bwd URG Flags|integer|
|Fwd Header Length40|integer|
|Bwd Header Length|integer|
|Fwd Packets/s|double|
|Bwd Packets/s|double|
|Min Packet Length|integer|
|Max Packet Length|integer|
|Packet Length Mean|double|
|Packet Length Std|double|
|Packet Length Variance|double|
|FIN Flag Count|integer|
|SYN Flag Count|integer|
|RST Flag Count|integer|
|PSH Flag Count|integer|
|ACK Flag Count|integer|
|URG Flag Count|integer|
|CWE Flag Count|integer|
|ECE Flag Count|integer|
|Down/Up Ratio|integer|
|Average Packet Size|double|
|Avg Fwd Segment Size|double|
|Avg Bwd Segment Size|double|
|Fwd Header Length61|integer|
|Fwd Avg Bytes/Bulk|integer|
|Fwd Avg Packets/Bulk|integer|
|Fwd Avg Bulk Rate|integer|
|Bwd Avg Bytes/Bulk|integer|
|Bwd Avg Packets/Bulk|integer|
|Bwd Avg Bulk Rate|integer|
|Subflow Fwd Packets|integer|
|Subflow Fwd Bytes|integer|
|Subflow Bwd Packets|integer|
|Subflow Bwd Bytes|integer|
|Init_Win_bytes_forward|integer|
|Init_Win_bytes_backward|integer|
|act_data_pkt_fwd|integer|
|min_seg_size_forward|integer|
|Active Mean|double|
|Active Std|double|
|Active Max|integer|
|Active Min|integer|
|Idle Mean|double|
|Idle Std|double|
|Idle Max|integer|
|Idle Min|integer|
|Label|string|

These values were extracted using the [get_data_header.py](./get_data_header.py)



- What features does it have?
- What features is it missing?
- Is the data good? Does it make sense?
- Is the data complete?
- Does it answer your question?

### Formatting the Data

  To make the data usable by WEKA, I will open it in Excel and export it as a CSV file format.

### Fixing Missing Data

  To fix any missing or corrupted data captured within this dataset, I will approximate the data using the mode and/or median.



  
