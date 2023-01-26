import decimal
import math
import statistics

def nlosrun():
    pexit = False
    while pexit == False:
        try:
            scinput = input("Input equation: ")
            if scinput == "?exit" or scinput == "?e":
                pexit = True
                continue
            if scinput == "":
                pass
            if scinput == "exit":
                print("Type ?e or ?exit to exit")
                continue
            scoutput = eval(scinput)
            ans = scoutput
            if isinstance(scoutput, (int, float)) and not isinstance(scoutput, bool):
                print(decimal.Decimal(str(scoutput)))
            else:
                print(str(scoutput))
        except SyntaxError:
            print("?SynErr")
        except NameError:
            print("?SynErr")
        except ValueError:
            return
        except BaseException as err:
            try:
                print(f"Could not eval\n{err=}\n{type(err)=}")
            except BaseException:
                print("Failed generating error message")

if __name__ == "__main__":
    print("This file is not meant to be run by Python.\nPlease install or open in NLOS to run this application.")
