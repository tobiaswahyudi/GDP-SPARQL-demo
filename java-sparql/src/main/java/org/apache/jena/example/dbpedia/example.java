package org.apache.jena.example.dbpedia;

import org.apache.http.util.EntityUtils;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.HttpClients;

public class example {
    public static void main(String[] args){
        HttpClient client = HttpClients.createDefault();

        HttpPost post = new HttpPost("http://localhost:3030/ds/sparql");
        StringEntity myEntity = new StringEntity(
                "query=select * where {?a ?b ?c} limit 5",
                ContentType.create("application/x-www-form-urlencoded", "UTF-8"));
        post.setEntity(myEntity);
        try {
            HttpResponse response = client.execute(post);
            String responseJSON = EntityUtils.toString(response.getEntity(), "utf8");
            System.out.print(response.getStatusLine());
        } catch (Exception err) {
            System.out.print("execution error");
        }
    }
}