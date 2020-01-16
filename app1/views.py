from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def detail(request):
    return render(request,'detail.html')

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split() #스플릿함수:텍스트.split 이렇게쓰면 띄어쓰기마다 나누어서 단어를 배열로 보여줌
    word_dictionary = {}
    for i in word_list:
        if i in word_dictionary:
            word_dictionary[i] += 1
        
        else:
            word_dictionary[i] = 1
    great_num=[]
    for word in word_list:
        if len(word)>=3:
            great_num.append(word)
    return render(request,'result.html',{'fulltxt': full_text,'total':len(word_list),'dictionary':word_dictionary.items(),'great_num':great_num})
    #get 방식은 보여져도 되는 부분의 text를 가져오는 방식이고
    #post 방식은 회원가입이나 로그인할때 보여지면 안되는 부분의 text를 가져오는 방식이다.
