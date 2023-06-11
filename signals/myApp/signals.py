# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import pre_delete, pre_init, pre_save, post_delete, post_init, post_save, pre_migrate, post_migrate
# from django.core.signals import request_started, request_finished, got_request_exception


# # ###################### METHOD 1 (register receiver using connect method) ######################
# def login_success_receiver(sender, request, user, **kwargs):
#     print("------------------------------------------------")
#     print("Login Successfull")
#     print(f"sender: {sender}")
#     print(f"request: {request}")
#     print(f"user: {user}")
#     print(f"kwargs: {kwargs}")
#     print("------------------------------------------------")

# # connecting our user to signals
# user_logged_in.connect(login_success_receiver, sender=User)


# # ###################### METHOD 2 (register receiver using decorator) ######################
# @receiver(user_logged_out, sender=User)
# def log_out(sender, request, user, **kwargs):
#     print("************************************************")
#     print("Logout Successfull")
#     print(f"sender: {sender}")
#     print(f"request: {request}")
#     print(f"user: {user}")
#     print(f"kwargs: {kwargs}")
#     print("************************************************")


# @receiver(user_login_failed)
# def login_failed(sender, credentials, request, **kwargs):
#     print("................................................")
#     print("LOGIN FAILED")
#     print(f"sender: {sender}")
#     print(f"credentials: {credentials}")
#     print(f"request: {request}")
#     print(f"kwargs: {kwargs}")
#     print("................................................")


# # Runs before our models are initialized (runs whenever our server reloads and runs for each model)
# # @receiver(pre_init, sender=User)
# # def at_beginning_init(sender, *args, **kwargs):
# #     print("Pre Init Signal Called")
# #     print(f"sender: {sender}")
# #     print(f"args: {args}")
# #     print(f"kwargs: {kwargs}")
# #     print("****************************************************************************************************************************************")

# # @receiver(post_init, sender=User)
# # def at_end_init(sender, *args, **kwargs):
# #     print("Post Init Signal Called")
# #     print(f"sender: {sender}")
# #     print(f"args: {args}")
# #     print(f"kwargs: {kwargs}")
# #     print("****************************************************************************************************************************************")


# @receiver(pre_save, sender=User)
# def at_beginning_save(sender, instance, **kwargs):
#     print("Pre Save Function Called")
#     print(f"sender: {sender}")
#     print(f"instance: {instance}")
#     print(f"kwargs: {kwargs}")
#     print("****************************************************************************************************************************************")


# @receiver(post_save, sender=User)
# def at_end_save(sender, instance, created, **kwargs):
#     if created:
#         print("Post Save Function Called")
#         print("*** New Record ***")
#         print(f"sender: {sender}")
#         print(f"instance: {instance}")
#         print(f"created: {created}")
#         print(f"kwargs: {kwargs}")
#         print("****************************************************************************************************************************************")
#     else:
#         print("Post Save Function Called")
#         print("*** Old Record ***")
#         print(f"sender: {sender}")
#         print(f"instance: {instance}")
#         print(f"created: {created}")
#         print(f"kwargs: {kwargs}")
#         print("****************************************************************************************************************************************")


# @receiver(pre_delete, sender=User)
# def at_beginning_delete(sender, instance, **kwargs):
#     print("Pre Delete Function Called")
#     print(f"sender: {sender}")
#     print(f"instance : {instance}")
#     print(f"kwargs: {kwargs}")
#     print("****************************************************************************************************************************************")


# @receiver(post_delete, sender=User)
# def at_end_delete(sender, instance, **kwargs):
#     print("Post Delete Function Called")
#     print(f"sender: {sender}")
#     print(f"instance: {instance}")
#     print(f"kwargs: {kwargs}")
#     print("****************************************************************************************************************************************")


# @receiver(request_started)
# def at_beginning_request(sender, environ, **kwargs):
#     print("_____________________________________________________________________________")
#     print("At Beginning Request")
#     print(f"sender: {sender}")
#     print(f"environ: {environ}")
#     print(f"kwargs: {kwargs}")

# @receiver(request_finished)
# def at_beginning_request(sender, **kwargs):
#     print("_____________________________________________________________________________")
#     print("At Ending Request")
#     print(f"sender: {sender}")
#     print(f"kwargs: {kwargs}")

# @receiver(got_request_exception)
# def at_beginning_request(sender, request, **kwargs):
#     print("_____________________________________________________________________________")
#     print("At Request Exception")
#     print(f"sender: {sender}")
#     print(f"request: {request}")
#     print(f"kwargs: {kwargs}")


# # When we run migrate command then for each app this method will run
# @receiver(pre_migrate)
# def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#     print("##############################################3")
#     print("Before install App")
#     print(f"sender: {sender}")
#     print(f"app_config: {app_config}")
#     print(f"verbosity: {verbosity}")
#     print(f"interactive: {interactive}")
#     print(f"using: {using}")
#     print(f"plan: {plan}")
#     print(f"apps: {apps}")
#     print(f"kwargs: {kwargs}")

# @receiver(post_migrate)
# def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#     print("##############################################3")
#     print("At End Migrate Flush")
#     print(f"sender: {sender}")
#     print(f"app_config: {app_config}")
#     print(f"verbosity: {verbosity}")
#     print(f"interactive: {interactive}")
#     print(f"using: {using}")
#     print(f"plan: {plan}")
#     print(f"apps: {apps}")
#     print(f"kwargs: {kwargs}")



