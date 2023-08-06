# Copyright 2016 Pavle Jonoski
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from threading import Condition


class Promise:
    def __init__(self):
        self.error = None
        self.__result = None
        self.__is_done = False
        self.__cw = Condition()

    @property
    def result(self):
        with self.__cw:
            while not self.__is_done:
                self.__cw.wait()

        if self.error:
            raise DistributedException(self.error, self.__result)
        return self.__result

    @property
    def is_done(self):
        return self.__is_done

    def complete(self, result=None, error=None):
        self.__is_done = True
        self.error = error
        self.__result = result
        with self.__cw:
            self.__cw.notify_all()



class DistributedException(Exception):

    def __init__(self, message, data=None):
        super(DistributedException, self).__init__(message)
        self.data = data
