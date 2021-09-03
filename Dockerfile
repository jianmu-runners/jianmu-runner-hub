FROM curlimages/curl:7.77.0

ADD publish /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/publish"]