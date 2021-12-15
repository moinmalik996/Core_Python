# class Mobile():

#     @classmethod
#     def show_model(cls):
#         print("RealMe X")


# realme = Mobile()
# Mobile.show_model()


class Mobile():

    _fp_ = "Yes"                                # class variable

    @classmethod                                # Decorator
    def is_fp(cls, ram):
        cls.ram = ram                             # cls is default
        print("Fingerprints :  ", cls._fp_)
        print("RAM  :  ", cls.ram)


Mobile.is_fp("4GB")