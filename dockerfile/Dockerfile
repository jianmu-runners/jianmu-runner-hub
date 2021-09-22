FROM curlimages/curl:7.77.0

ADD script/publish /usr/local/bin/
USER root
RUN apk add openssl
ENTRYPOINT ["sh"]
CMD ["/usr/local/bin/publish"]