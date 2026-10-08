package chatbot;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class chatbot {
	public static void main(String[] args) throws IOException, InterruptedException{
	boolean flag=true;
	while(flag) {
		Scanner sc=new Scanner(System.in);


		 System.out.println("----chatBot-----");


		 System.out.print("User : ");


		 String message=sc.next();


		 String apikey=System.getenv("GROQ_API_KEY");


		 


		 HttpClient httpClient=HttpClient.newHttpClient();


		 


		 String json = """


		 {


		 "model": "openai/gpt-oss-20b",


		 "messages": [


		 {


		 "role": "user",


		 "content": "%s"


		 }


		 ]


		 }


		 """.formatted(


		 message.replace("\"", "\\\"")


		 );


		 


		 HttpRequest request = HttpRequest.newBuilder()


		 .uri(URI.create(


		 "https://api.groq.com/openai/v1/chat/completions"


		 ))


		 .header("Authorization", "Bearer " + apikey)


		 .header("Content-Type", "application/json")


		 .POST(HttpRequest.BodyPublishers.ofString(json))


		 .build();


		 


		 HttpResponse<String> response = httpClient.send(


		 request,


		 HttpResponse.BodyHandlers.ofString()


		 );


		 


		 //System.out.println("\nGroq: ");


		 //System.out.println(response.body());


		 


		 String body = response.body();


		 


		 int start = body.indexOf("\"content\":\"") + 11;


		 int end = body.indexOf("\"", start);


		 


		 String message2 = body.substring(start, end);


		 


		 System.out.println("Groq: " + message2);


		 


		 


		 


		 System.out.println();

	}

		}
		
	}
