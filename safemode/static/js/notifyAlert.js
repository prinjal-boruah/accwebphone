
 document.addEventListener('DOMContentLoaded', function() {
      const webSocketBridge = new channels.WebSocketBridge();  
      


      console.log("------In Notify Fun()-------");

     


      webSocketBridge.connect('/notifications/');
      webSocketBridge.listen(function(action, stream) {
        console.log("RESPONSE:", action);


         
        if(action.user_id == 0){
              n=0;
            }else{

            //var str1 = "http://192.168.20.182:7000/videostream/"+action.user_id+"/";
            var str1 = "http://106.51.37.192:7000/videostream/"+action.user_id+"/";
            var str2 = window.location.href;
            console.log("Loc1 :: "+str1);
            console.log("Loc2 :: "+str2);

            var n = str1.localeCompare(str2);

            console.log("Result :: "+ n);

            }
        if(n == 0){

          if(action.event == "New Text") {          
          console.log("----------In New Text Incident-----------");  

           var div_id122 = '#med-content'+action.user_id;
           console.log("Div name :: "+div_id122);

           console.log("### in IF Block--------");
           $('#med-content').text ( action.url ); 
            

            }
           else  if(action.event == "New Image") {          
          console.log("----------In New Image Incident-----------");     
          // http://192.168.20.182/ipcam/images/gokeralPopup.jpg
          
          document.getElementById("med-content").innerHTML = "";
          var x = document.createElement("IMG");
            x.setAttribute("src", action.url);
            x.setAttribute("width", "570");
            x.setAttribute("height", "320");
            x.setAttribute("alt", "The Pulpit Rock");
            document.getElementById("med-content").appendChild(x);            

         //$('#med-txt').text ( "Welcome Image" );  
          
        } 
        else if(action.event == "New Video") {          
          console.log("----------In New Video Incident-----------");     

          //document.getElementById("med-txt").text = "";
          document.getElementById("med-content").innerHTML = "";
         
          var x = document.createElement("VIDEO");

          x.setAttribute("src",action.url);
          x.setAttribute("type","video/ogg");
          x.setAttribute("autoplay", "autoplay");
          document.getElementById("med-content").appendChild(x);

          /*if (x.canPlayType("video/ogg")) {
            x.setAttribute("src",action.url);
          } else {
            x.setAttribute("src",action.url);
          }*/

          
         /* if (x.canPlayType("video/ogg")) {
            x.setAttribute("src",action.url);
          } if (x.canPlayType("video/mp4")) {
            x.setAttribute("src",action.url);
          }else {
            x.setAttribute("src",action.url);
          }  */
          


          // x.setAttribute("width", "480");
          // x.setAttribute("height", "320");
          
          // x.setAttribute("class", "myVideo"); 
          


         //$('#med-txt').text ( "Welcome Video" );  
          
        }

      }
        


        /*if(action.event == "New Call Video") {          
          console.log("----------In New Call Video Incident-----------");     

         $('#med-content').text ( "Welcome Call Video" );  
          
        }

        if(action.event == "Stop Event") {          
          console.log("----------In New Default-----------");     

          $('#med-content').text ("Welcome To BNATCL");  
          
        }

        if(action.event == "New Animation") {          
          console.log("----------In New Animation Incident-----------");     

         $('#med-content').text ( "Welcome Animation" );  
          
        }*/


        

      })


      document.ws = webSocketBridge; /* for debugging */
    })



function getStatus(){

  var fsm = document.getElementById("med-content");

  if(fsm.requestFullscreen)
    fsm.requestFullscreen();
  else if(fsm.mozRequestFullScreen)
    fsm.mozRequestFullScreen();
  else if(fsm.webkitRequestFullscreen)
    fsm.webkitRequestFullscreen();
  else if(fsm.msRequestFullscreen)
    fsm.msRequestFullscreen();

  var cnt_type = document.getElementById("cnt_type").value;
  var cnt_url = document.getElementById("cnt_url").value;
  var cnt_id = document.getElementById("cnt_id").value;

  console.log("Type ::-----------> "+cnt_type);

  if(cnt_id){
    
  }

      if(cnt_type == "stop") {          
          console.log("----------In DB Default-----------");     

          $('#med-content').text ("Welcome To BNATCL");  
          
        }

        if(cnt_type == "text") {          
          console.log("----------In DB Text Incident-----------");     

          $('#med-content').text ( cnt_url );  
          
        }
        if(cnt_type == "image") {          
          console.log("----------In DB Image Incident-----------");     
          // http://192.168.20.182/ipcam/images/gokeralPopup.jpg
          
          document.getElementById("med-content").innerHTML = "";
          var x = document.createElement("IMG");
            x.setAttribute("src", cnt_url);
            x.setAttribute("width", "570");
            x.setAttribute("height", "320");
            x.setAttribute("alt", "The Pulpit Rock");
            document.getElementById("med-content").appendChild(x);            

         //$('#med-txt').text ( "Welcome Image" );  
          
        }
        if(cnt_type == "animation") {          
          console.log("----------In DB Animation Incident-----------");     

         $('#med-content').text ( "Welcome Animation" );  
          
        }
        if(cnt_type == "video") {          
          console.log("----------In DB Video Incident-----------");     

          //document.getElementById("med-txt").text = "";
          document.getElementById("med-content").innerHTML = "";
         
          var x = document.createElement("VIDEO");

          /*if (x.canPlayType("video/ogg")) {
            x.setAttribute("src",cnt_url);
          } else {
            x.setAttribute("src",cnt_url);
          }*/


          if (x.canPlayType("video/ogg")) {
            x.setAttribute("src",cnt_url);
          } if (x.canPlayType("video/mp4")) {
            x.setAttribute("src",cnt_url);
          }else {
            x.setAttribute("src",cnt_url);
          } 

          // x.setAttribute("width", "480");
          // x.setAttribute("height", "320");
          x.setAttribute("autoplay", "autoplay");
          document.getElementById("med-content").appendChild(x);


         //$('#med-txt').text ( "Welcome Video" );  
          
        }
        if(cnt_type == "callvideo") {          
          console.log("----------In DB Call Video Incident-----------");     

         //$('#med-content').text ( "Welcome Call Video" );  
          
        }



}
  



 

// API Calls

/*


{
    "media_type": "text",
    "url": "Hi Prinjal !!!"
}

{
    "media_type": "image",
    "url": "http://192.168.20.182/ipcam/images/gokeralPopup.jpg"
}


{
    "media_type": "video",
    "url": "http://192.168.20.182:8109/stream"
}

{
    "media_type": "stop",
    "url": "stop"
}

{
    "media_type": "animation",
    "url": "URL STRING"
}

{
    "media_type": "callvideo",
    "url": "URL STRING"
}


*/