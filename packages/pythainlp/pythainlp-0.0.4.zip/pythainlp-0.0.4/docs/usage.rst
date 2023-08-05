=====
Usage
=====

To use PyThai-NLP in a project::

    import pythainlp
	
    # ตัดคำ
	
    from pythainlp.segment import segment
	
    a = 'ฉันรักภาษาไทยเพราะฉันเป็นคนไทย'
	
    b = segment(a)
	
    print(b) # ['ฉัน', 'รัก', 'ภาษาไทย', 'เพราะ', 'ฉัน', 'เป็น', 'คนไทย']
	
    # Postaggers ภาษาไทย
	
    from pythainlp.postaggers import tag
	
    print(tag('คุณกำลังประชุม')) #ค ุณ/PPRS กำลัง/XVBM ประชุม/VACT
	
    # หาคำที่มีจำนวนการใช้งานมากที่สุด
	
    from pythainlp.rank import rank
	
    aa = rank(b)
	
    print(aa) # Counter({'ฉัน': 2, 'ไทย': 2, 'เป็น': 1, 'รัก': 1, 'ภาษา': 1, 'เพราะ': 1, 'คน': 1})
	
    # ทับศัพท์เสียงไทยในภาษาอังกฤษ (ยังไม่รองรับเสียงสระ)
	
    from pythainlp.romanization import romanization
	
    b=romanization("ต้นกก")
	
    print(b) # tonkok
	
    # แก้ไขปัญหาการพิมพ์ลืมเปลี่ยนภาษา
	
    from pythainlp.change import *
	
    a="l;ylfu8iy["
	
    a=texttothai(a)
	
    b="นามรสนอำันี"
	
    b=texttoeng(b)
	
    print(a) # สวัสดีครับ
	
    print(b) # ok,iloveyou
	
    # เปลี่ยนตัวเลขเป็นตัวอักษรภาษาไทย (เงินบาท)
	
    from pythainlp.number import numtowords
	
    print("5611116.50")
	
    print(numtowords(5611116.50)) # ห้าล้านหกแสนหนึ่งหมื่นหนึ่งพันหนึ่งร้อยสิบหกบาทห้าสิบสตางค์