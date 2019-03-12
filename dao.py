#!/usr/bin/python


#~ format pliku to liczba:reszta
#~ 
#~ czynnosci:
#~ - wylistuj czynnosci i czasy
#~ - czy jest czynnosc
#~ - dodaj czynnosc
#~ - usun
#~ - zzeruj czas
#~ - 
#~ - 
#~ 


from pprint import pprint


SEP = ':'

# TODO: get/set to property
# TODO: comments up to eng


class TaskEntry:


    def set_time(self, _tasktime):
        self.tasktime = _tasktime

    def set_string(self, _taskstring):
        self.taskstring = _taskstring


    # TODO: obsolete
    def get_time(self):
        return self.tasktime

    # TODO: obsolete
    def get_string(self):
        return self.taskstring


    def load_content(self, _taskcontent):
        splitted = _taskcontent.split(SEP, 1)
        self.tasktime = splitted[0]
        self.taskstring = splitted[1]
        
    def throwup_content(self):
        return self.tasktime + SEP + self.taskstring




class DAO:


    def __init__(self, _datacontent):
        '''
        _datacontent = [                     taskEntries = [
            '648:abcdefghi',                     entry{'648', 'abcdefghi'},
            '517:QjhWkizN5t',        ==>         entry{'517', 'QjhWkizN5t'},
            '323:dwcIY99gTN1',                   entry{'323', 'dwcIY99gTN1'},
            '653:UlfY2UvMfeuX'                   entry{'653', 'UlfY2UvMfeuX'}
        ]                                    ]
        '''
        self.taskEntries = []

        for line in _datacontent:
            entry = TaskEntry()
            entry.load_content(line.strip())
            self.taskEntries.append(entry)


    def is_empty(self):
        if not self.taskEntries:
            return True
        else:
            return False


    def find(self, _taskstring):
        for entry in self.taskEntries:
            if _taskstring == entry.taskstring:
                return entry


    def what_u_have(self):      # TODO: probably remove
        for entry in self.taskEntries:
            print [entry.tasktime, entry.taskstring]


    def add_entry(self, _tasktime, _taskstring):
        if self.find(_taskstring):
            raise Exception(_taskstring + ' already present')
        entry = TaskEntry()
        entry.set_time(_tasktime)
        entry.set_string(_taskstring)
        self.taskEntries.append(entry)


    def remove_entry(self, _taskstring):
        entry_looked_for = self.find(_taskstring)
        if not entry_looked_for:
            raise Exception(_taskstring + ' does not exist')
        self.taskEntries.remove(entry_looked_for)


    def reset_time(self, _taskstring):
        entry_looked_for = self.find(_taskstring)
        if not entry_looked_for:
            raise Exception(_taskstring + ' does not exist')
        idx = self.taskEntries.index(entry_looked_for)
        self.taskEntries[idx].set_time('0')


    def update_time(self, _taskstring, _time):
        entry_looked_for = self.find(_taskstring)
        if not entry_looked_for:
            raise Exception(_taskstring + ' does not exist')
        idx = self.taskEntries.index(entry_looked_for)
        self.taskEntries[idx].set_time(_time)


    def advance_time(self, _taskstring, _time):
        entry_looked_for = self.find(_taskstring)
        if not entry_looked_for:
            raise Exception(_taskstring + ' does not exist')
        idx = self.taskEntries.index(entry_looked_for)
        self.taskEntries[idx].set_time(str(int(self.taskEntries[idx].get_time())+int(_time)))


    # def write_datafile(self):
    #     df = open(self.datafile, 'w')
    #     for entry in self.taskEntries:
    #         df.write(entry.throwup_content() + '\n')
    #     df.close()

        



if __name__ == '__main__':


    # DAO is_empty(), read_datafile(), find()
    DATAFILE = 'tempdata.txt'

    # dao = DAO(DATAFILE)
    # print 'is empty?: ' + str(dao.is_empty())
    # dao.read_datafile()
    # print 'is empty?: ' + str(dao.is_empty())

    query1 = dao.find('dwa wyrazy')
    if query1:
        print 'time =', query1.tasktime, 'string =', query1.taskstring
    else:
        print 'Nic, nic'

    query2 = dao.find('tego nie bedzie')
    if query2:
        print 'time =', query2.tasktime, 'string =', query2.taskstring
    else:
        print 'Nic, nic'

    print

    # DAO what_u_have(), add_entry()
    dao.what_u_have()

    print
    #

    dao.add_entry('1234', 'fiszi fiszi')
    try:
        dao.add_entry('123', 'dwa wyrazy')
    except Exception as ex:
        print ex
    dao.what_u_have()

    print

    # DAO remove_entry()
    dao.remove_entry('dwa wyrazy')
    try:
        dao.remove_entry('takiego to nie bedzie na pewno')
    except Exception as ex:
        print ex
    dao.what_u_have()

    print

    # DAO reset time
    dao.reset_time('yyyy')
    try:
        dao.reset_time('takiego to nie bedzie na pewno')
    except Exception as ex:
        print ex
    dao.what_u_have()

    print

    # DAO update time
    dao.update_time('zzzzz', '777')
    try:
        dao.reset_time('takiego to nie bedzie na pewno')
    except Exception as ex:
        print ex
    dao.what_u_have()

    print

    # DAO advance time
    dao.advance_time('xxx', '4')
    try:
        dao.reset_time('takiego to nie bedzie na pewno')
    except Exception as ex:
        print ex
    dao.what_u_have()

    print

    # DAO store
    # dao.write_datafile()
