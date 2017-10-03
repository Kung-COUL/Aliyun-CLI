sed -i.bak '/init.coul.com/d' ~/.ssh/known_hosts
scp -r ~/github/woocommerce/* root@init.coul.com:
ssh -i ~/.ssh/Tom.pem root@init.coul.com
