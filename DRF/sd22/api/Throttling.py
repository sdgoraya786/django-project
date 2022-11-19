from rest_framework.throttling import UserRateThrottle

class SDRateThrottle(UserRateThrottle):
    scope = 'sd'