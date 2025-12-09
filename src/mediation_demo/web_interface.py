from cmd import PROMPT
import gradio as gr
from convokit import Corpus, Forecaster
from gradio import ChatMessage
from openai import OpenAI
from src.mediation_demo.utils import buyer_prompt



HTML_NAV = """
<div class="topnav">
  <header>
    <nav class="nav">
      <!-- Logo / icon on the left -->
      <div href="#home" class="menu-bar-item logo">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          width="50"
          height="50"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linecap="butt"
          stroke-linejoin="round">
          <circle cx="12" cy="12" r="8.5" />
          <path d="M8 4a14 14 0 0 1 0 16" />
          <path d="M16 4a14 14 0 0 0 0 16" />
          <path d="M4 12h16" />
        </svg>
      </div>

      <div class="menu-center">
        <a href="#home" class="menu-bar-item">Featured</a>
        <a href="#news" class="menu-bar-item">Products</a>
        <a href="#contact" class="menu-bar-item">About</a>
        <a href="#about" class="menu-bar-item active">Profile</a>
        <a href="#about" class="menu-bar-item">Contact Us</a>
      </div>
    </nav>
  </header>
</div>
"""

CSS_nav = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500&display=swap');

.topnav {
    background-color: #4838F5;
    border-radius: 0;
    margin: 0;                
    padding: 10px 20px;
    position: fixed;          
    top: 0;
    left: 0;
    width: 100%;               
    box-sizing: border-box;
    z-index: 1;               
}

.topnav .nav {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;        /* needed for absolute-positioned logo */
}


.menu-bar-item.logo {
    position: absolute;
    left: 20px;
    display: flex;
    align-items: center;
    padding-right: 8px;
}


.menu-center {
    display: flex;
    align-items: center;
    gap: 40px;
}

.menu-bar-item {
    color: #f2f2f2;
    font-size: 22px;
    padding: 16px 0px;
    text-decoration: none;
    font-family: "IBM Plex Sans", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-weight: 300; 
}

.menu-bar-item.active {
    color: #f2f2f2;
    background-color: #3528BE;
    padding: 16px 20px;
    border-radius: 4px;
}

.menu-bar-item:hover {
    text-decoration: underline;
}
"""
HTML_sidebar ="""
<div class="sidenav">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <a href="#"><i class="fa-regular fa-user"></i>John B.</a>
  <hr style="width:90%; text-align:center; margin: 5px auto;">
  <a href="#">Personal Information</a>
  <a href="#">Addresses</a>
  <a href="#">Wishlist</a>
  <a href="#">My Orders</a>
</div>

""" 

CSS_sidebar = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500&display=swap');
.sidenav {
  height: auto;
  width: 220px;
  position: fixed;
  z-index: 0;
  top: 80px;            
  left: 0;        
  bottom: 0;    
  background-color: #D5CC89;
  overflow-x: hidden;
  padding-top: 20px;
  font-family: "IBM Plex Sans", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 300; /* light weight */
}


.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 18px;
  color: #f2f2f2;
  display: block;
}

.sidenav a:hover {
  color: #f1f1f1;
  
}


.fa-regular.fa-user {
        margin-right: 10px; 
        vertical-align: middle;
}
"""
HTML_thank_you ="""
<div class="main">
  <div class="content-row">
    <div class="thank-you">
      <h1 style="font-size:40px; color: black;">Thank you for your purchase, John!</h1>
      <h2 style = "color: black;">Order ID: 2637839300</h2>
    </div>
    <button class="rounded-green-box">
      Delivered
    </button>
</div>
"""



CSS_thank_you = """
.main {
  display: flex;
  flex-direction: row;
  width: 200px;
  margin-left: 220px;          /* same as sidebar width */
  margin-right: 40px;          /* give it room on the right */
  margin-top: 80px;            /* space for fixed nav bar */
  box-sizing: border-box;
}

/* Lay out text + button in a row */
.content-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;  
}
.thank-you {
  margin-right: 50px;
}

.rounded-green-box {
  background-color: #D0F0C0;
  border-radius: 20px;
  width: 400px;
  height: 40px;
  padding: 5px 20px;
  color: #00A86B;
  margin: 20px 0 0 0;
  border: none;
}
"""

HTML_product_card = """
<div class="main product-card">
  <div class="product-card-row">
    <div class="product-card-content">
      <span>
        <img
          src="https://slimages.macysassets.com/is/image/MCY/products/4/optimized/9362384_fpx.tif?$filterlrg$&wid=327"
          alt="Product Image"
          style="width:70%;"
        >
      </span>http://127.0.0.1:7860/#
    </div>
    <div class="product-card-content">
      <div class="product-card-content-row style">
        <span class="order-summary-text">QTY</span>
         <span class= "order-summary-text">Price</span>
                <span class="order-summary-text">Amount</span>
      </div>
      <div class="product-card-content-row">
        <hr class="product-card-divider">
      </div>
      <div class="product-card-content-row">
        <span class="order-summary-text">$24.99</span>
        <span class="order-summary-text">1</span>
        <span class="order-summary-text">$24.99</span>
      </div>
      <div class="product-card-content-row">
        <span class="order-summary-text">
          <h2 class="order-summary-text">Ship to:</h2>
          <br id="product-br">
          <span class="order-summary-text">2512 Ocean Avenue, Los Angeles, CA, 98132, USA</span>
        </span>
      </div>
    </div>
  </div>
</div>
"""


CSS_product_card = """
.main.product-card {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-left: 220px;
  width: 700px;
  margin-top: 30px;
  padding: 0 10px;
  box-sizing: border-box;
  vertical-align: top;
}

.product-card-row {
  display: flex;
  gap: 50px;
  justify-content: center;
  font-size:22px;
}

.product-card-content-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  
  gap: 10px;
}

/* Divider line */
.product-card-divider {
  flex: 1;
  border: none;
  border-top: 1px solid #b0b0b0;
  margin: 10px 0;
}

/* Optional: styling for the <br> */
#product-br {
  display: block;
  margin-top: 4px;
}

.address-text {
  font-size: 20px;
  font-weight: 400;
}
.order-summary-text {
  color: #63666A;
}
"""
HTML_order_summary ="""
<div class="main order-summary">
  <div class="order-summary-card">
    <h2>Order Summary</h2>

    <div class="summary-row">
      <span>Subtotal</span>
       <span>$24.99</span>
      <span>$24.99</span>

    </div>
    <div class="summary-row">
      <span>Discount</span>
      <span>$0.00</span>
      <span>-$1.00</span>
    </div>
    <div class="summary-row">
      <span>Free Shipping</span>
      <span>$0.00</span>
    </div>
    <div class="summary-row">
      <span>Tax</span>
      <span>$0.87</span>
      <span>$0.87</span>
    </div>

    <hr class="summary-divider">

    <div class="summary-row total">
      <span>Total</span>
      <span>$25.86</span>
    </div>
  </div>
</div>
"""

CSS_order_summary = """
.order-summary-card span {
  color: #63666A;
}

.main.order-summary {
  margin-left: 220px;     
  width: 700px;
  height: 300px;
  margin-top: 20px;
  padding: 0 10px;
  box-sizing: border-box;
}

/* Card container */
.order-summary-card {
  background-color: #d3d3d3;
  border-radius: 20px;
  padding: 16px 20px;
  font-family: "IBM Plex Sans", system-ui, -apple-system, BlinkMacSystemFont,
               "Segoe UI", sans-serif;
  font-size: 22px;
  color: #63666A;              /* NEW: base text color for the whole card */
}

.order-summary-card h2 {
  margin: 0 0 12px 0;
  font-size: 22px;
  color: #63666A;              /* keep same, explicit */
}

.summary-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
  font-size: 16px;
  color: #63666A;              /* changed from #888B8D */
}

.summary-divider {
  border: none;
  border-top: 1px solid #b0b0b0;
  margin: 10px 0;
}

.summary-row.total {
  font-weight: 600;
  margin-top: 4px;
  color: #63666A;              /* changed from black */
}
"""


HTML_review = """
<div class="review-card">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <p style ="font-size: 22px; color: #63666A;"> Like what you got? We would love to know! </p>
  <Button class="rate-review-button"><i class="fa-solid fa-star"></i>Rate and Review!</Button>
  <div class = "return-policy">
    <Button class="return-policy button"><i class="fa-regular fa-circle-question"></i></i>Return Policy: Active Until Dec 15th </Button>
  </div>
</div>
"""

CSS_review = """
.review-card {
  display: flex;
  flex-direction: column;
  margin-left: 250px;
  margin-top: 220px;
  padding: 25px;              
  width: 500px;
  height: 200px;
  text-align: center;
  color: #63666A;             
  box-sizing: border-box;
  background-color: #d3d3d3;
  border-radius: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.review-card-text {
  font-size: 16px;
  font-weight: 400;
  color: #63666A;
}
.rate-review-button {
  background-color: #CFE5FF;
  color: #4838F5;
  margin: 10px 40px;
  border-radius: 20px;
  font-size: 20px;
  font-weight: 20;
}

.fa-regular.fa-circle-question {
  margin-right: 8px; /* Adjust as needed for spacing after the icon */
}

.fa-solid.fa-star {
  color: #4838F5;
  margin-right: 8px; /* Adjust as needed for spacing after the icon */
}

.return-policy.button {
  margin: 10px 40px;
  background-color: #63666A;
  border-radius: 20px;
  height: 25px;
  line-height: 5px;     
  font-size: 13px;
  font-weight: 400;
  text-align: center;   
  padding: 0px 16px;      
}
"""

custom_css = """
.gradio-container {
    background-color: #f5f5f5
}

#my-chat {
  width: 300px;
  height: 600px;
  margin: 0px 350px;
}"""


client = OpenAI()

buyer_conversation = client.conversations.create(
  model="gpt-4.1-mini",
  items=[{"type": "message", "role": "system", "content": buyer_prompt}]
)
buyer_conversation_id = buyer_conversation.id

mediator_conversation = client.conversations.create(
  model="gpt-4.1-mini",
  items=[{"type": "message", "role": "system", "content": mediator_prompt}]
)
mediator_conversation_id = mediator_conversation.id

buyer_response = client.responses.create(
    model="gpt-4.1-mini",
    conversation=conversation.id,
    input="Explain rate limits like I'm 12.",
)



# def calculate_derailment(corpus: Corpus, threshold: float) -> float:
#     return

#     def to_corpus(history: Dict[str,Any]) -> Corpus:
#           return

def generate_response(prompt: str, history: list[NormalizedMessageDict]) ->  list[NormalizedMessageDict]:
      buyer_response = client.response.create(
      model="gpt-4.1-mini", 
      conversation=conversation.id, 
      input=prompt)
      buyer_text = buyer_response.output_text
      #need to append response to chatbot conversation
      history.append({"role":"assistant","content":buyer_text})
      # derailed_flag = calculate_derailment(conversation.id, threshold=0.5)
      # if derailed_flag:
      #   mediator_response(message, history)
      # if we need mediaition agent, we need to wait on him
      return buyer_text, history
      

def mediator_response(message, history) -> gr.NormalizedMessageDict:
   #running in the background, not blocking main thread
  return

with gr.Blocks() as demo:
  gr.HTML(html_template=HTML_NAV,css_template=CSS_nav)
  with gr.Row():
    with gr.Column():
      gr.HTML(html_template=HTML_sidebar, css_template=CSS_sidebar)
      gr.HTML(html_template=HTML_thank_you, css_template=CSS_thank_you)
      gr.HTML(html_template=HTML_product_card, css_template=CSS_product_card)
      gr.HTML(html_template=HTML_order_summary, css_template=CSS_order_summary)
    with gr.Column():
      gr.HTML(html_template=HTML_review, css_template=CSS_review)
      chatbot = gr.Chatbot(max_height=500, resizable=True, layout="bubble", elem_id="my-chat")
      prompt = gr.Textbox(lines=1, placeholder="Chat Message")
      prompt.submit(generate_response, inputs=[prompt, chatbot], outputs=[chatbot])
      prompt.change(lambda: gr.update(value=""), outputs=[prompt])


demo.launch(css=custom_css) 

    

# Side bar component
# Menu bar 
# Thank you next 
# Product Card
# Order summary 
# Leave rating
# Leave review


# Funtional:
#"Chat with us Button" -> Chat Interface Here

# create response API for chatbot as seller perspective:
# creat MCP for derailement detection
# create mediation agent to create respone to chatbot


#chat interface:
