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


#### What features does it have?

The features that this dataset have are that it has many different factors for each flag, and specifically the rate and flow for each individual packet that is being sent over the wire. This allows for more specific details to be obtained while analyzing the data.

#### What features is it missing?

The features that are missing would be the context around the packets. Such as, what is the traffic that is being generated used for? What production area is this information gathered from?

#### Is the data good? Does it make sense?

Based on the data that is gathered, it does make sense though a quick glance from reading the files from CSV. 

### Formatting the Data

  To make the data usable by WEKA, I will open it in Excel and export it as a CSV file format.
  
  There is one issue while loading the dataset: 

    The column `Fwd Header Length` appears more than once which will cause an issue. Because of this, I changed the headers to Fwd Header Length 1 and 2.

  The only other change made is to remove the initial space for the headers in each column that were either prepended or appended to the end of the label.

### Fixing Missing Data

  To fix any missing or corrupted data captured within this dataset, I will approximate the value of the rows that may have missing data using the mean and/or median of preexisting data.

  |Header|Amount Missing|Percent Missing|
  |-|-|-|
  |Flow Bytes|4|0%|

Compared to the rest of the dataset, this is so insignificantly small that it can be removed from the dataset and have virtually no effect on the outcome of the entire dataset. However with WEKA, there is a built in function to keep this data within this dataset and to approximate the values.

In order to fix these values, we can use `RemoveWithValues -S 0.0 -C last -L first-last` to approximate these rows as needed.

While using this unsupervised filter, we can change this setting to have the proper attribute index to do more with this data.

The current configuration for this filter are as follows:

|Option|Value|
|-|-|
|attributeIndex|21|
|debug|False|
|doNotCheckCapabilities|False|
|dontFilterAfterFirstBatcH|False|
|invertSelection|False|
|matchMissingValues|True|
|modifyHeader|False|
|nominalIndices|first-last|
|splitPoint|0.0|

At this point, the data has been cleaned and the Flow Bytes truly have no missing data.

  |Header|Amount Missing|Percent Missing|
  |-|-|-|
  |Flow Bytes|0|0%|

  

## Exploring Different Models within the Dataset

At this point, I am looking for trends or patterns within the data to be able to make smart decisions from it. Such as what different factors or categories of each data can provide useful insights to what can contribute to a Denial of Service attack. 

### Supervised Models

We have enough data to determine the conditions that need to be met to consiter traffic to be a part of a DDoS attack. We have several models available to show us whatever kind of information we want to gather useful insight behind the data.

#### J48

A J48 Model will help us visualize how traffic can be consitered malicious. 
> [Source](<Supervised Models/J48/output.txt>)

Configuration:

|Option|Value|
|-|-|
|batchSize|100|
|binarySplits|False|
|collapseTree|True|
|confidenceFactor|0.25|
|debug|False|
|doNotCheckCapabilities|False|
|doNotMakeSplitPointActualValue|False|
|minNumObj|2|
|numDecimalPlaces|2|
|numFolds|3|
|reducedErrorPruning|False|
|saveInstanceData|False|
|seed|1|
|subtreeRaising|True|
|unpruned|True|
|useLaplace|False|
|useMDLcorrction|True|

Although this chart is useful, the amount of leaves and the overall size of this tree is so large that it provides no useful data on its own. The tree produced a chart that has 96771 leaves and an overall size of 96787. In order to make this more useful we need to either narrow it down by quite a bit or to find sets of rules that make this more useful.

