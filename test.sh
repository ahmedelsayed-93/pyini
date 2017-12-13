echo "public_var ${public_var}, private_var ${private_var}"

if [[ "${private_var}" == 'password']]; then
  echo "doesn't changed"
else
  echo "changed"
 fi
