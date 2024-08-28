'''
Created on 28 May 2024

@author: pakala
'''
import restapi
app = restapi.create_app()
app.run(host="0.0.0.0", port=8001, debug=True)
