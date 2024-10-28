from django.shortcuts import render,redirect,get_object_or_404

from store.forms import SignUpForm,SignInForm,UserProfileForm,ProjectForm

from django.urls import reverse_lazy

from store.models import Project

from django.views.generic import View,FormView,CreateView,TemplateView

from django.contrib.auth import authenticate,login,logout

# Create your views here.

class SignUpView(CreateView):

    template_name="register.html"

    form_class=SignUpForm

    success_url=reverse_lazy("login")

    # def get(self,request,*args,**kwargs):

    #     form_instance=self.form_class

    #     return render(request,self.template_name,{"form":form_instance})

    # def post(self,request,*args,**kwargs):

    #     form_instance=self.form_class(request.POST)

    #     if form_instance.is_valid():

    #         form_instance.save()

    #         print("account created")

    #         return redirect("signup")

    #     else:

    #         print("failed to create account")

    #         return render(request,self.template_name,{"form":form_instance})

class SignInView(FormView):

    template_name='login.html'

    form_class=SignInForm

    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            uname=form_instance.cleaned_data.get("username")

            pwd=form_instance.cleaned_data.get("password")

            user_object=authenticate(username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect("index")
        
        return render(request,self.template_name,{"form":form_instance})


class IndexView(TemplateView):

    template_name="index.html"

    def get(self,request,*args,**kwargs):

        qs=Project.objects.all().exclude(developer=request.user)

        return render(request,self.template_name,{"data":qs})

# def logout_view():

#     logout(request)

#     return redirect("login")

class LogoutView(View):

    def get(self,request,*args,**kwargs):
        
        logout(request)

        return redirect("login")


class ProfileEditView(View):

    template_name="profileedit.html"

    form_class=UserProfileForm

    def get(self,request,*args,**kwargs):
        
        user_instance=request.user.profile

        form_instance=UserProfileForm(instance=user_instance)

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        user_instance=request.user.profile

        form_instance=UserProfileForm(request.POST,instance=user_instance,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("index")

        return render(request,self.template_name,{"form":form_instance})


class ProjectView(View):

    template_name="project_add.html"

    form_class=ProjectForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST,files=request.FILES)

        form_instance.instance.developer=request.user

        if form_instance.is_valid():

            form_instance.save()
            
            return redirect("index")
        
        return render(request,self.template_name,{"form":form_class})


class MyprojectListView(View):

    template_name="my_project_list.html"

    def get(self,request,*args,**kwargs):

        qs=Project.objects.filter(developer=request.user)

        return render(request,self.template_name,{"data":qs})


class ProjectUpdateView(View):

    template_name="project_update.html"

    form_class=ProjectForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        project_obj=Project.objects.get(id=id)

        form_instance=self.form_class(instance=project_obj)

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        project_obj=Project.objects.get(id=id)

        form_instance=self.form_class(request.POST,instance=project_obj,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("my-work")

        return render(request,self.template_name,{"form":form_instance})

class ProjectDetailView(View):

    template_name="product_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Project.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})


class WIshlistView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        project_object=get_object_or_404(Project,id=id)

        request.user.basket.basket_item.create(project_object=project_object)

        print("item added to wishlist")

        return redirect("index")


class WishlistItemView(View):

    template_name="mywishlist.html"

    def get(self,request,*args,**kwargs):

        qs=request.user.basket.basket_item.filter(is_order_placed=False)

        return render(request,self.template_name,{"data":qs})

















