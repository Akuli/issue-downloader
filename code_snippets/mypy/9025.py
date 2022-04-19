class A:
   def func_on_win_only() -> str:
      assert sys.platform == "win32"
      return sys.getwindowsversion()
