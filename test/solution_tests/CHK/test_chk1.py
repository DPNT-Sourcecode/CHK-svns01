from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("AAABBBCD") == 240 # 130+45+30+20+15
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout('aa') == -1
        assert checkout_solution.checkout("-") == -1

        assert checkout_solution.checkout("AAAAAAAAABEE") == 460 # 9A, 2E (B is free)=> 200+130+50+80
        assert checkout_solution.checkout("EE") == 80

        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("AFF") == 70
        assert checkout_solution.checkout("ZZXZ") == 62 # 45 + 1X (17)