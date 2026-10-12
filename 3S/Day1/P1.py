#Type

print(type(3.4))

#Type Hits
model_name:str = "Gemini_2.0_Flash"
temp:float = 0.7
max_tokens:int = 1024
isstream:bool = True
content_box:str|None = None
print(type(model_name))

#String : Immutable
#String Formatting
  #Old Style
print("Model Name: %s" % model_name)
name = "Sandeep Kumar KH"
print("I am, '%s'" % name)


#New Style
print(f"Model Name: {model_name}")
print(f"I am, '{name}'")

#Expression Inside f-string
wordlimit=250
print(f"{'Over Limit' if wordlimit>200 else 'Within Limit'}")

wordlimit=150
print(f"{'Over Limit' if wordlimit>100 else 'Within Limit'}")


data = {"Name":"xyxy","topic":"RAG"}
print(f"Name:{data["Name"]}")
print(f"Topic:{data["topic"]}")


pi = 3.14159
print(f"pi:{pi:.2f}")


# Dedugging  = 

temp = 0.7
print(f"{temp=}")

# Multi line f-string formatting

user_input = "What is Langchain?"
content_text = "Langchain is a framework for building LLM apps"
system_prompt = f"""
you are helpful AI tutor.
context provided: {content_text}
student question:{user_input}
Instruction:
-Answer based only on the context above
-It the answer is not in the context, say "I don't know"
-Keep your answers under 3 sentences
""".strip()
print(system_prompt)


#lists: ordered, mutable,  heterogenous sequesces
# Function :

def build_prompt(topic:str,world_limit:int=150)->str:
    return f"Write about {topic}, with atmost {world_limit} words"


print(build_prompt("GEN_AI"))
print(build_prompt("prompt engg",world_limit=2300))


# Brushup following concepts:
## *args
## **kwargs
