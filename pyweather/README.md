# PyWeather Application
Application to display the weather status.

### Environment 
EKS cluster is created through Terraform for the deployment. 

### Backend
The backend service uses a ClusterIP to make the service accessible only within the cluster.

### Frontend
The frontend service has a configurable backend URL variable that can be configured with an environment variable. 

## Running It All
Everything can be set up with the following command:  
`kubectl apply -f weather-frontend/manifests/ -f weather-backend/manifests/`  
The frontend is exposed on port `30003` and can then be hit by using a node IP with this port.  
`http://{nodeIP}:30003/{city}`  
`http://{nodeIP}:30003/toronto`