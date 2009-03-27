from django.conf import settings

def intense_debate_acct(request):
    return {'INTENSE_DEBATE_ACCT': settings.INTENSE_DEBATE_ACCT}
