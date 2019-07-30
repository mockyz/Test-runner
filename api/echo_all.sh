
for json in request_j/*
do
    cat $json >> all_requests.txt
    echo "\n" >>all_requests.txt
done