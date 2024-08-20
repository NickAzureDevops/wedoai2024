# Azure DevOps Pipeline Monitoring with Azure AI

This repository provides steps to set up an Azure DevOps pipeline and use Azure AI to monitor and analyze performance metrics, as well as predict future trends.

## Steps to Monitor Azure DevOps Pipeline with Azure AI

### Analyze Data with Azure AI

1. **Run the Azure DevOps Pipeline**:
   - Execute the `dev.yaml` pipeline in Azure DevOps.
   - The pipeline uses two main scripts to collect and upload data:
     - `collect_data.py`: Collects data from the Azure DevOps pipeline.
     - `upload_data.py`: Uploads the collected data to an Azure Storage Account.

   After running the pipeline, the data will be collected and uploaded to the Azure Storage Account.

2. **Set Up Azure Machine Learning Workspace**:
   - Go to the [Azure Portal](https://portal.azure.com/).
   - Create a new Azure Machine Learning workspace.

3. **Collect Data from Azure Storage Account**:
   - Import the data from the Azure Storage Account to Azure Machine Learning Studio.

4. **Create a New Experiment**:
   - Open Azure Machine Learning Studio.
   - Create a new experiment and import the data from the Azure Storage Account.

5. **Train a Predictive Model**:
   - Use the data to train a predictive model. You can use built-in algorithms or custom scripts to analyze the data.

6. **Deploy the Model**:
   - Once the model is trained, deploy it as a web service for real-time predictions.

### Visualize Data with Azure Application Insights

1. **Create Dashboards and Reports**:
   - Use the built-in tools in Azure Application Insights to create dashboards and reports to visualize the data and identify trends.


   