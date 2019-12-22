from Host import Host

def test_GameCreated():
    host = Host()
    
    p0_join_request = {
        'Action'        :    'NewPlayer',
        'Credential'    :    '193f647e-2a67-4cec-aef9-cabae8ab1a78',
    }
    
    p0_join_response = host.handle(p0_join_request)
    p0_token = p0_join_response.get('PlayerToken', None)
    assert type(p0_token) == str
    
    p0_check_request = {
        'Action'        :    'CheckWaitingStatus',
        'PlayerToken'   :    p0_token,
    }
    
    p0_check_response = host.handle(p0_check_request)
    assert p0_check_response.get('Matched', None) == False
    
    p1_join_request = {
        'Action'        :    'NewPlayer',
        'Credential'    :    '4fbcb042-124d-4a70-a370-42e6f15b27b7',
    }
    
    p1_join_response = host.handle(p1_join_request)
    p1_token = p1_join_response.get('PlayerToken', None)
    assert type(p1_token) == str
    
    p0_check_response2 = host.handle(p0_check_request)
    assert p0_check_response2.get('Matched', None) == True
    
    p1_check_request = {
        'Action'        :    'CheckWaitingStatus',
        'PlayerToken'   :    p1_token,
    }
    
    p1_check_response = host.handle(p1_check_request)
    assert p1_check_response.get('Matched', None) == True
