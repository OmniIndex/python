Creating and Maintaining encryption keys
========================================

This is by no means an exhaustive review of creating and maintaining encryption keys.  It is a quick overview of the process.  For more information, please see the following resources:

.. _restructuredtext: 
    
    * Google cloud https://cloud.google.com/storage/docs/encryption/customer-managed-keys
    * AWS https://docs.aws.amazon.com/mgn/latest/ug/ebs-encryption-kms.html
    * Azure https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-configure-existing-account?tabs=azure-portal
    * Oracle https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm
    * National Cyber Security Centre https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/password-managers

Creating a key
--------------

This sample would use the gcloud cli:

.. code-block:: bash

    gcloud kms keyrings create my-keyring --location global
    gcloud kms keys create my-key --location global --keyring my-keyring --purpose encryption

This sample would create a key using openssl (Linux, MacOS etc)

.. code-block:: bash

    openssl genrsa -out private.key 2048

This is the code to use powershell on Windows:

.. code-block:: powershell

    $key = New-Object System.Security.Cryptography.RSACryptoServiceProvider 2048
    $key.ExportParameters($true) | Export-Clixml -Path private.key




