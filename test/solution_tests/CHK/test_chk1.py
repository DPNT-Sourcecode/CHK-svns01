from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("AAABBBCD") == 240
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout('aa') == 100
        assert checkout_solution.checkout("-") == -1



