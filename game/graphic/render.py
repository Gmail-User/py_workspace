# render.py

MODULE_NAME = 'render'

def render_test():
    print('- render::render_test invoked.')

    # 1. 절대경로방식으로 패키지를 import
    # from game.sound.echo import echo_test

    # 2. 상대경로방식으로 패캐지를 import
    from ..sound.echo import echo_test
    
    echo_test()

    pass