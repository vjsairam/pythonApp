# PyWeather Application
Application to display the weather status. https://github.com/vjsairam/pythonApp/tree/master/pyweather

### Environment 
EKS cluster is created through Terraform for the deployment. https://github.com/vjsairam/pythonApp/tree/master/terraform-eks-cluster

### Backend
The backend service uses a ClusterIP to make the service accessible only within the cluster. https://github.com/vjsairam/pythonApp/tree/master/pyweather/weather-backend

### Frontend
The frontend service has a configurable backend URL variable that can be configured with an environment variable. https://github.com/vjsairam/pythonApp/tree/master/pyweather/weather-frontend

## Running It All
Everything can be set up with the following command:  
`kubectl apply -f pyweather/weather-frontend/manifests/ -f pyweather/weather-backend/manifests/`  
The frontend is exposed on port `30003` and can then be hit by using a node IP with this port.  
`http://{nodeIP}:30003/{city}`  
`http://{nodeIP}:30003/toronto`