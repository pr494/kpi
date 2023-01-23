from django.shortcuts import render
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from .models import Question
import json
from .serializers import RegisterSerializer
import re
A="""{"type":"scaffold","args":{"appBar":{"type":"app_bar","args":{"title":{"type":"text","args":{"text":"Form"}}}},"backgroundColor":"#e0e0e0","body":{"type":"safe_area","args":{"bottom":true},"child":{"type":"form","child":{"type":"single_child_scroll_view","args":{"padding":[16,0]},"child":{"type":"container","args":{"alignment":"topCenter","width":"infinity"},"child":{"type":"container","args":{"constraints":{"maxWidth":450}},"child":{"type":"column","args":{"mainAxisSize":"min"},"children":[{"type":"sized_box","args":{"height":16}},{"type":"sized_box","args":{"height":8}},{"type":"material","args":{"borderRadius":16,"color":"#fff","elevation":4,"margin":[0,8],"padding":16},"child":{"type":"column","args":{"mainAxisSize":"min"},"children":["""
C=""" ] } }, { "type": "elevatedbutton", "id": "submit_button", "args": { "onPressed": "${simple PrintMessage({"dropdown button_form_field":email_type,"text_form_field":email_address})}" }, "child": { "type": "container", "args": { "alignment": "center", "width": "infinity" }, "child": { "type": "save_context", "args": { "key": "form_context" }, "child": { "type": "text", "args": { "text": "Submit" } } } } } ] } } } } } } } }"""
edit_text= {
  "type": "text_form_field",
  "id": "first_name",
  "args": {
    "decoration": {
      "hintText":"John",
      "labelText":"First Name",
      "suffixIcon":{
        "type":"icon_button",
        "args":{
          "icon":{
            "type":"icon",
            "args":{
              "icon":{
                "codePoint":57704,
                "fontFamily":"MaterialIcons",
                "size": 50
              }
            }
          },
          "onPressed":"${set_value('first_name','')}"
        }
      }
    },
    "validators": [
      {
        "type":"required"
      }
    ]
  }
},

@api_view(['GET'])
def get_user(request, kpi_id=None):
            Child = Question.objects.filter(kpi_id=kpi_id)
            serializer = RegisterSerializer(Child,many=True)
            #return Response({"data":serializer.data})
            B=""
            for passenger in serializer.data:
                if passenger['element_type'] == "text":
                    B = B+str(edit_text)
                    
                elif passenger['element_type'] == "phone":
                    B = B+str(edit_text)
            valuestr=A+B+C
            y = re.sub(r'\\','', valuestr)
                    
            return Response({"status":200,"success":True,"data":[{"id":"form1","form":(y)}]}) 
                
                    
    
        


        