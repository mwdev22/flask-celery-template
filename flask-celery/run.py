from simapp.saconnector.app import create_app
import subprocess
from celery.bin import worker
from celery import current_app

PARTNER_NAMES = ['SMSMAN', 'SMSH'] 


app = create_app()


if __name__ == '__main__':
    # starting the worker with python3 run.py in another process
    # subprocess.Popen(['celery', '-A', 'app.make_celery', 'worker', '--loglevel=INFO'])
    
    app.run(debug=True)
    
    '''
    processes = []
    start_port = 6000
    
    for name in PARTNER_NAMES:
        app = create_app(partner_name=name)
        command = f"gunicorn -b 127.0.0.1:{start_port} 'app:app'"
        process = subprocess.Popen(command, shell=True)
        processes.append(process)
        start_port += 1

    for process in processes:
        process.wait()
    '''