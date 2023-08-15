from django.shortcuts import render , HttpResponse
from home.models import contact
from home.models import cand_ans
from home.models import cand_bank
from home.models import ques_ans
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from static import nlp
from static import rand
from static import calc
from django.http import StreamingHttpResponse
from static import gesture

my_area = []
us_ps = []
authe = []
s=25




def video_stream(request):
    return StreamingHttpResponse(gesture.generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

# Create your views here.
def homepage(request):
    context={
        "variable" : "Smart Hire"
    }
    return render(request , "index.html" , context)
    #return HttpResponse("This is Homepage")

def contacts(request):
    global s
    s = 25
    authe.clear()

    if request.method == "POST":
        #reset.reset_auto_increment()
        #calc.reset_auto_increment(cand_ans)
        # check if user has entered correct credentials
        us_ps.clear()
        cand = request.POST.get('username')
        us_ps.append(cand)
        pas = request.POST.get('password')
        us_ps.append(pas)
        user = authenticate(username = cand , password = pas)

        if user is not None:
            try:
                contact.objects.get(username = us_ps[0])
                return redirect ("final2.html")
            except:
                cand_ans.objects.all().delete()
                authe.append(1)
                return redirect ("ques1.html")
        
        else:
            alert_message = "Invalid credentials. Please try again."
            return render(request, 'contact.html', {'show_alert': True, 'alert_message': alert_message})

            # return render(request , "contact.html")
    



    context={
        "variable" : "Smart Hire"
    }
    return render(request , "contact.html" , context)

def ques1(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans1 = request.POST.get('ans1')
        key1 = nlp.give_keywords(ans1) 
        obj1 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans1 , keywords_ans = key1)
        obj11 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans1 , keywords_ans = key1)
        obj1.save()
        obj11.save()
        authe.append(1)
        return redirect("ques2.html")
        # messages.success(request, "Your answer has been saved")
    
    tup1 = rand.for_ques1()
    id = tup1[0]
    sec_lst = tup1[1]
    item = ques_ans.objects.get(qa_id=id)
    my_area.append(id)
    my_area.append(sec_lst)
    my_area.append(item.ques)

    context={
        "q1" : item.ques,
    }
    if len(authe) == 1:
        return render(request , "ques1.html" , context) 
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect ("ques3.html")
    elif len(authe) == 4:
        return redirect ("ques4.html")
    elif len(authe) == 5:
        return redirect ("ques5.html")
    elif len(authe) == 6:
        return redirect ("ques6.html")
    elif len(authe) == 7:
        return redirect ("ques7.html")
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")
        


def ques2(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans2 = request.POST.get('ans2')
        key2 = nlp.give_keywords(ans2)
        obj2 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans2 , keywords_ans = key2)
        obj12 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans2 , keywords_ans = key2)
        obj2.save()
        obj12.save()
        authe.append(1)
        return redirect("ques3.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup2 = rand.for_ques2(my_area[1])
        id = tup2[0]
        sec_lst = tup2[1]
        item2 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item2.ques)

    except IndexError:
        return redirect ("ques1.html")


    context={
        "q2" : item2.ques
    }
    if len(authe) == 2:
        return render(request , "ques2.html" , context)
    elif len(authe) == 1:
        return redirect ("ques1.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect ("ques3.html")
    elif len(authe) == 4:
        return redirect ("ques4.html")
    elif len(authe) == 5:
        return redirect ("ques5.html")
    elif len(authe) == 6:
        return redirect ("ques6.html")
    elif len(authe) == 7:
        return redirect ("ques7.html")
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")

def ques3(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans3 = request.POST.get('ans3')
        key3 = nlp.give_keywords(ans3)
        obj3 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans3 , keywords_ans = key3)
        obj13 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans3 , keywords_ans = key3)
        obj3.save()
        obj13.save()
        authe.append(1)
        return redirect("ques4.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup3 = rand.for_ques2(my_area[1])
        id = tup3[0]
        sec_lst = tup3[1]
        item3 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item3.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q3" : item3.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return render(request , "ques3.html" , context)
    elif len(authe) == 4:
        return redirect ("ques4.html")
    elif len(authe) == 5:
        return redirect ("ques5.html")
    elif len(authe) == 6:
        return redirect ("ques6.html")
    elif len(authe) == 7:
        return redirect ("ques7.html")
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")
    

def ques4(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans4 = request.POST.get('ans4')
        key4 = nlp.give_keywords(ans4)
        obj4 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans4 , keywords_ans = key4)
        obj14 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans4 , keywords_ans = key4)
        obj4.save()
        obj14.save()
        authe.append(1)
        return redirect("ques5.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup4 = rand.for_ques2(my_area[1])
        id = tup4[0]
        sec_lst = tup4[1]
        item4 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item4.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q4" : item4.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return render(request , "ques4.html" , context)
    elif len(authe) == 5:
        return redirect ("ques5.html")
    elif len(authe) == 6:
        return redirect ("ques6.html")
    elif len(authe) == 7:
        return redirect ("ques7.html")
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")

def ques5(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans5 = request.POST.get('ans5')
        key5 = nlp.give_keywords(ans5)
        obj5 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans5 , keywords_ans = key5)
        obj15 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans5 , keywords_ans = key5)
        obj5.save()
        obj15.save()
        authe.append(1)
        return redirect("ques6.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup5 = rand.for_ques2(my_area[1])
        id = tup5[0]
        sec_lst = tup5[1]
        item5 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item5.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q5" : item5.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return redirect("ques4.html")
    elif len(authe) == 5:
        return render(request , "ques5.html" , context)
    elif len(authe) == 6:
        return redirect ("ques6.html")
    elif len(authe) == 7:
        return redirect ("ques7.html")
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")
    

def ques6(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans6 = request.POST.get('ans6')
        key6 = nlp.give_keywords(ans6)
        obj6 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans6 , keywords_ans = key6)
        obj16 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans6 , keywords_ans = key6)
        obj6.save()
        obj16.save()
        authe.append(1)
        return redirect("ques7.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup6 = rand.for_ques2(my_area[1])
        id = tup6[0]
        sec_lst = tup6[1]
        item6 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item6.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q6" : item6.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return redirect("ques4.html")
    elif len(authe) == 5:
        return redirect("ques5.html")
    elif len(authe) == 6:
        return render(request , "ques6.html" , context)
    elif len(authe) == 7:
        return redirect ("ques7.html")
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")
    

def ques7(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans7 = request.POST.get('ans7')
        key7 = nlp.give_keywords(ans7)
        obj7 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans7 , keywords_ans = key7)
        obj17 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans7 , keywords_ans = key7)
        obj7.save()
        obj17.save()
        authe.append(1)
        return redirect("ques8.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup7 = rand.for_ques2(my_area[1])
        id = tup7[0]
        sec_lst = tup7[1]
        item7 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item7.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q7" : item7.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return redirect("ques4.html")
    elif len(authe) == 5:
        return redirect("ques5.html")
    elif len(authe) == 6:
        return redirect("ques6.html")
    elif len(authe) == 7:
        return render(request , "ques7.html" , context)
    elif len(authe) == 8:
        return redirect ("ques8.html")
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")
    

def ques8(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans8 = request.POST.get('ans8')
        key8 = nlp.give_keywords(ans8)
        obj8 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans8 , keywords_ans = key8)
        obj18 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans8 , keywords_ans = key8)
        obj8.save()
        obj18.save()
        authe.append(1)
        return redirect("ques9.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup8 = rand.for_ques2(my_area[1])
        id = tup8[0]
        sec_lst = tup8[1]
        item8 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item8.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q8" : item8.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return redirect("ques4.html")
    elif len(authe) == 5:
        return redirect("ques5.html")
    elif len(authe) == 6:
        return redirect("ques6.html")
    elif len(authe) == 7:
        return redirect("ques7.html")
    elif len(authe) == 8:
        return render(request , "ques8.html" , context)
    elif len(authe) == 9:
        return redirect ("ques9.html")
    elif len(authe) == 10:
        return redirect ("ques10.html")
    


def ques9(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans9 = request.POST.get('ans9')
        key9 = nlp.give_keywords(ans9)
        obj9 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans9 , keywords_ans = key9)
        obj19 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans9 , keywords_ans = key9)
        obj9.save()
        obj19.save()
        authe.append(1)
        return redirect("ques10.html")
        # messages.success(request, "Your answer has been saved")
    
    try:
        tup9 = rand.for_ques2(my_area[1])
        id = tup9[0]
        sec_lst = tup9[1]
        item9 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item9.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q9" : item9.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return redirect("ques4.html")
    elif len(authe) == 5:
        return redirect("ques5.html")
    elif len(authe) == 6:
        return redirect("ques6.html")
    elif len(authe) == 7:
        return redirect("ques7.html")
    elif len(authe) == 8:
        return redirect("ques8.html")
    elif len(authe) == 9:
        return render(request , "ques9.html" , context)
    elif len(authe) == 10:
        return redirect ("ques10.html")
    

def ques10(request):

    if request.method == "POST":
        global s
        s = gesture.score
        ans10 = request.POST.get('ans10')
        key10 = nlp.give_keywords(ans10)
        obj10 = cand_ans(q_id=my_area[0] , ques = my_area[2] , ans = ans10 , keywords_ans = key10)
        obj20 = cand_bank(user = us_ps[0] , q_id=my_area[0] , ques = my_area[2] , ans = ans10 , keywords_ans = key10)
        obj10.save()
        obj20.save()
        authe.append(1)
        return redirect("final.html")
        # messages.success(request, "Your answer has been saved")

    try:
        tup10 = rand.for_ques2(my_area[1])
        id = tup10[0]
        sec_lst = tup10[1]
        item10 = ques_ans.objects.get(qa_id=id)
        
        my_area.clear()
        my_area.append(id)
        my_area.append(sec_lst)
        my_area.append(item10.ques)
        
    except IndexError:
        return redirect ("ques1.html")


    context={
        "q10" : item10.ques
    }
    if len(authe) == 1:
        return redirect("ques1.html")
    elif len(authe) == 2:
        return redirect ("ques2.html")
    elif len(authe) == 0:
        return redirect ("contact.html")
    elif len(authe) == 3:
        return redirect("ques3.html")
    elif len(authe) == 4:
        return redirect("ques4.html")
    elif len(authe) == 5:
        return redirect("ques5.html")
    elif len(authe) == 6:
        return redirect("ques6.html")
    elif len(authe) == 7:
        return redirect("ques7.html")
    elif len(authe) == 8:
        return redirect("ques8.html")
    elif len(authe) == 9:
        return redirect("ques9.html")
    elif len(authe) == 10:
        return render(request , "ques10.html" , context)

def final(request):
    authe.clear()

    if request.method == "POST":
        #calc.reset_auto_increment(cand_ans)
        #ans4 = request.POST.get('ans4')
        #obj4 = cand_ans(q_id=4 , ques = "Who?" , ans = ans4)
        #obj4.save()
        return redirect("index.html")
        # messages.success(request, "Your answer has been saved")
    score = 0
    for i in range (1,800):
        try:
            sl = cand_ans.objects.get(id = i)
            ms = ques_ans.objects.get(qa_id = sl.q_id)

            master = eval(ms.ans)
            slave = eval(sl.keywords_ans)
            
            count_sc = calc.count_matching_strings(master,slave)

            if count_sc >= 5:
                score+=7.5
            else:
                score+=(count_sc * 1.5)
        
        except:
            continue


    context={
        "var" : score
    }
    #try:
    #print(us_ps[0])
    #print(us_ps[1])
    try:
        contact.objects.get(username = us_ps[0])
        return redirect ("final2.html")
    except:
        score = score + round(s,1)
        person = contact(username = us_ps[0] , password = us_ps[1] , score = score)
        person.save()


    # if contact.objects.get(username = us_ps[0]) is not None:
    #     return redirect ("final2.html")
    # else:
    #     person = contact(username = us_ps[0] , password = us_ps[1] , score = score)
    #     person.save()
    #except:
        #return redirect("final2.html")



    return render(request , "final.html" , context)

def final2(request):
    authe.clear()
    if request.method == "POST":
        return redirect("index.html")
    
    return render(request , "final2.html")
    