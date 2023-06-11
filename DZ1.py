"""ways to format strings."""

#old string format
norway_text = 'Automatisering akselererer %syeblikket da roboter vil ' \
               'erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')

#string formatting with the format method
norway_text1 = 'Automatisering akselererer {0}yeblikket da roboter vil ' \
              'erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ')

#string formatting method f
textx = 'ø'
texty = 'å'
textz = 'Æ'
norway_text2 = f'Automatisering akselererer {textx}yeblikket da roboter vil ' \
              f'erobre planeten v{texty}r. ({textz})'
print(norway_text)
print(norway_text1)
print(norway_text2)

