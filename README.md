# SMB111-project
Final project SMB111
Berthier Théo


## Create functionapp

Créer une fonction app à partir d'un resource group ainsi qu'un "storage account", l'exemple suivant est une fonctionapp qui sera fait pour fonctionner avec nodejs et du javascrpt

```bash
az functionapp create --name simple-interest --storage-account myresourcesgroupb3b7 --resource-group myResourcesGroup --consumption-plan-location eastus --runtime node
```
## Create function

Ensuite l'initialisation d'une fonction ce fait comme cela

```bash
func init
1.
2.
3. node
4. python
5. powershell

3

creation ....
```

Les fichiers concernant la fonction son initialisé il suffit de créer une nouvelle fonction 

```bash
func new <func_name>

10. http trigger
```

Un fichier est créer il suffit de modifier le fichier index.js pour ajouter sa fonction

ensuite il est possible de tester en local la fonction 
```bash
func start &> output.txt &
```
après une url est donnée dans output.txt pour requéter l'api 

```bash
curl "http://localhost:7071/api/simple-interest?principal=5000&rate=0.14&term=5"
```
Une fois vérifier on peut publier la fonction 

```bash
func azure functionapp publish simple-interest
Getting site publishing info...
Creating archive for current directory...
Uploading 1.38 KB [###############################################################################]
Upload completed successfully.
Deployment completed successfully.
Syncing triggers...
Functions in simple-interest:
    simple-interest - [httpTrigger]
        Invoke url: https://<uri>.azurewebsites.net/api/simple-interest
```
Retourver le token liée à la fonction 

```bash
az functionapp keys list --name simple-interest --resource-group myResourcesGroup   
```

Ensuite le test 

```bash
curl "https://simple-interest.azurewebsites.net/api/simple-interest?code=<token>&principal=5000&rate=0.14&term=5"
3500.0000000000005
```

