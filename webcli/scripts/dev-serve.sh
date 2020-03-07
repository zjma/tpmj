# Script to prepare Vue envvars then start serving.
# Designed to be used by npm scripts.

apiserver=$1

if [ -z "$apiserver" ]
then
    echo "API server URL not specified."
    exit 1
fi

echo VUE_APP_WEBCLI_VERSION=`cat ../Version`* > .env.local
echo VUE_APP_API_SERVER_URL=$apiserver >> .env.local
vue-cli-service serve
