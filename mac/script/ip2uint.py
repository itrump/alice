ip = '192.168.0.1'

total = 0
print 'ip is %s' % ip
for item in ip.split('.'):
    num = int(item)
    print 'total:%s, num:%s' % (total, num)
    total = total << 8
    print 'after shift total:%s' % total
    total += num
    print 'after add num[%s], total:%s' % (num, total)
