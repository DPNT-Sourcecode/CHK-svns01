from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("AAABBBCD") == 300 # 130+90+45+20+15
