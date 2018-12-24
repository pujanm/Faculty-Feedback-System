from django.shortcuts import render, redirect, HttpResponse
from .models import Feedback, UserProfile, TeacherProfile, Subject
from .forms import UserForm, UserProfileForm, TeacherProfileForm
from .filters import TeacherProfileFilter
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


def index(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return redirect("admin_analytics")
        else:
            if TeacherProfile.objects.all().filter(user=request.user).count() == 0:
                f = Feedback.objects.filter(student=UserProfile.objects.filter(user=request.user))
                subjects_done_feedback = [i.subject.name for i in f]
                username = request.user
                u = UserProfile.objects.filter(user=username)
                fname = u[0].fname
                lname = u[0].lname
                subject_list = [i.name for i in u[0].subject.all()]
                teacher_list = TeacherProfile.objects.all()
                for i in subject_list:
                    if i in subjects_done_feedback:
                        try:
                            subject_list.remove(i)
                        except ValueError:
                            pass
                print(subject_list)
                if request.POST:
                    u = u[0]
                    s = request.POST.get('subject')
                    t = request.POST.get('teacher')
                    f1 = request.POST.get('f1')
                    f2 = request.POST.get('f2')
                    f3 = request.POST.get('f3')
                    f4 = request.POST.get('f4')
                    f5 = request.POST.get('f5')
                    f6 = request.POST.get('f6')
                    f7 = request.POST.get('f7')
                    f8 = request.POST.get('f8')
                    f9 = request.POST.get('f9')
                    sug = request.POST.get('sug')
                    tea = TeacherProfile.objects.filter(fname=t.split(" ")[0])
                    print(tea)
                    sub = Subject.objects.filter(name=s)
                    print(sub)
                    f = Feedback.objects.create(
                        student=u,
                        subject=sub[0],
                        teacher=tea[0],
                        res1=f1,
                        res2=f2,
                        res3=f3,
                        res4=f4,
                        res5=f5,
                        res6=f6,
                        res7=f7,
                        res8=f8,
                        res9=f9,
                        sug=sug
                    )
                    f.save()
                    return redirect('analytics')
                context = {
                    'fname': fname,
                    'lname': lname,
                    'teacher_list': teacher_list,
                    'subject_list': subject_list
                }
                return render(request, 'appOne/dashboard.html', context)
            else:
                return redirect('teacher_analytics')
    else:
        return redirect('signup')



def analytics(request):

    if Feedback.objects.all().count() != 0:
        subject_list = []
        avg_sub = []
        if request.user.is_authenticated():
            user = request.user
            student = UserProfile.objects.filter(user=user)
            subjects = [i.name for i in student[0].subject.all()]
            for subject in subjects:
                sub_obj = Subject.objects.filter(name=subject)
                sub = Feedback.objects.filter(subject=sub_obj, student=student)
                if sub.count() != 0:
                    print(sub)
                    sum = 0
                    sum = sub[0].res1 / 5 + sub[0].res2 / 5  + sub[0].res3 / 5 + sub[0].res4 / 5 + sub[0].res5 / 5 + sub[0].res6 / 5 + sub[0].res7 / 5 + sub[0].res8 / 5 + sub[0].res9 / 5
                    avg = sum / 9
                    avg_sub.append(round(avg * 100))
                    subject_list.append(subject)
                    print(avg_sub)
            context = {
                    'feedback': avg_sub,
                    'subject': subject_list,
                    'f': ''
                }
            print(context['subject'])
            return render(request, 'appOne/analytics.html', context)
        else:
            return redirect('signup')
    else:
        if request.user.is_authenticated():
            return render(request, 'appOne/analytics.html', {'f': 'No Fucks Yet!!'})
        else:
            return redirect('signup')


def teacher_analytics(request):

    if Feedback.objects.all().count() != 0:
        avg_sub = []
        subject_list = []
        if request.user.is_authenticated():
            user = request.user;
            teacher = TeacherProfile.objects.filter(user=user)
            subjects = [i.name for i in teacher[0].subject.all()]
            print(teacher[0].fname + " " + teacher[0].lname)
            fname = teacher[0].fname
            lname = teacher[0].lname
            for subject in subjects:
                sub_obj = Subject.objects.filter(name=subject)
                sub = Feedback.objects.filter(subject=sub_obj, teacher=teacher)
                if sub.count() != 0:
                    print(sub)
                    sum = 0
                    sum = sub[0].res1 / 5 + sub[0].res2 / 5  + sub[0].res3 / 5 + sub[0].res4 / 5 + sub[0].res5 / 5 + sub[0].res6 / 5 + sub[0].res7 / 5 + sub[0].res8 / 5 + sub[0].res9 / 5
                    avg = sum / 9
                    avg_sub.append(round(avg * 100))
                    subject_list.append(subject)
                    print(avg_sub)
            context = {
                    'feedback': avg_sub,
                    'subject': subject_list,
                    'fname': fname,
                    'lname': lname,
                    'f': ''
                }
            return render(request, 'appOne/teacher_analytics.html', context)
        else:
            return redirect('signup')
    else:
        if request.user.is_authenticated():
            return render(request, 'appOne/teacher_analytics.html', {'f': 'No Fucks Yet!!'})
        else:
            return redirect('signup')


def get_teacher_name(request, subject):
    s = Subject.objects.filter(name=subject)
    if s.count() != 0:
        t = TeacherProfile.objects.filter(subject=Subject.objects.filter(name=subject)[0])
        teacher_names = [i.fname + ' ' + i.lname for i in t]
    else:
        teacher_names = ['No Teacher Found']
    print(teacher_names)
    return HttpResponse(json.dumps({'teacher_names': teacher_names}), content_type="application/json")


def get_subject_on_semester(request, semester):
    subs = [i.name for i in Subject.objects.filter(semester=semester)]
    f = Feedback.objects.filter(student=UserProfile.objects.filter(user=request.user))
    subjects_done_feedback = [i.subject.name for i in f]
    final = [i for i in subs if i not in subjects_done_feedback]
    print(final)

    return HttpResponse(json.dumps({'subjects': final}), content_type="application/json")


def teacher_detailed_analytics(request, subject):
    subject = Subject.objects.filter(name=subject)
    user = request.user
    teacher = TeacherProfile.objects.filter(user=user)

    feedback = Feedback.objects.filter(teacher=teacher, subject=subject)
    arr = [0, 0, 0, 0, 0]
    count_arr = ["One", "Two", "Three", "Four", "Five"]
    for i in feedback:
        sum = 0
        sum = i.res1 + i.res2 + i.res3 + i.res4 + i.res5 + i.res6 + i.res7 + i.res8 + i.res9
        avg = round(sum/9.0)
        arr[avg - 1] += 1

    print(arr)
    context = {
        'subject_name': subject[0].name,
        'fname': teacher[0].fname,
        'lname': teacher[0].lname,
        'arr': arr,
        'count_arr': count_arr
    }
    return render(request, "appOne/teacher_detailed_analytics.html", context)


def admin_analytics(request):
    if request.user.is_authenticated():
        subject = Subject.objects.all()
        context = {
            "subject": subject,
        }
        return render(request, "appOne/admin_analytics.html", context)
    else:
        return redirect('signup')


def admin_analytics_detailed(request, subject):
    if request.user.is_authenticated():
        subject = Subject.objects.filter(name=subject)
        subject_students = subject[0].subject_students.all()
        subject_students_users = [i.user.username for i in subject_students]
        print(subject_students_users)

        subject_feedback = Feedback.objects.filter(subject=subject)
        subject_feedback_users = [i.student.user.username for i in subject_feedback]
        print(subject_feedback_users)

        # subject_feedback_users_notfilled_name = []
        subject_feedback_users_notfilled = []
        for i in subject_students_users:
            if i not in subject_feedback_users:
                user = User.objects.filter(username=i)
                studentPro = UserProfile.objects.filter(user=user)[0]
                # subject_feedback_users_notfilled_name.append(studentPro.fname + " " + studentPro.lname)
                subject_feedback_users_notfilled.append([i, (studentPro.fname + " " + studentPro.lname)])

        context = {
            "sapid": subject_feedback_users_notfilled,
            "subject": subject[0],
        }
        return render(request, "appOne/admin_analytics_detailed.html", context)

    else:
        return redirect('signup')


def teacherSignup(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        teacher_form = TeacherProfileForm(data=request.POST)

        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            login(request, user)
            return redirect('teacher_analytics')
    else:
        user_form = UserForm()
        teacher_form = TeacherProfileForm()
    return render(request, 'appOne/teacher_signup.html', {'user_form': user_form,
                                                          'teacher_form': teacher_form})


def signup(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'appOne/signup.html', {'user_form': user_form,
                                                  'profile_form': profile_form})


@login_required
def logOut(request):
    logout(request)
    return redirect('signup')


def teacherLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_analytics')
            else:
                return redirect('teacher_analytics')
        else:
            return render(request, 'appOne/teacher_login.html', {'i': 'Invalid Password/SAP ID'})
    return render(request, 'appOne/teacher_login.html', {'i': ''})


def logIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        try:
            u = UserProfile.objects.all().filter(user=user)
        except:
            print("User does not exist!")
        if(u.count() == 0):
            return render(request, 'appOne/login.html', {'i': 'Invalid Password/SAP ID'})
        user = authenticate(username=username, password=password)

        if user and (u.count() != 0):
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'appOne/login.html', {'i': 'Invalid Password/SAP ID'})
    return render(request, 'appOne/login.html', {'i': ''})
