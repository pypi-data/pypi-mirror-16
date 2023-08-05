﻿"""Assignment helper functions for Selenium testing."""

import random
import string
import time
import inspect
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait


class Assignment(object):
    """Shortcut functions to add, edit, and delete assignments."""

    READING = 'reading'
    HOMEWORK = 'homework'
    EXTERNAL = 'external'
    EVENT = 'event'

    BEFORE_TITLE = 'title'
    BEFORE_DESCRIPTION = 'description'
    BEFORE_PERIOD = 'period'
    BEFORE_SECTION_SELECT = 'section'
    BEFORE_READING_SELECT = 'reading'
    BEFORE_EXERCISE_SELECT = 'exercise'
    BEFORE_URL = 'url'
    BEFORE_STATUS_SELECT = 'status'

    WAIT_TIME = 15

    TUTOR_SELECTIONS = 'tutor'

    PUBLISH = 'publish'
    CANCEL = 'cancel'
    DRAFT = 'draft'
    DELETE = 'delete'

    def __init__(self):
        """Provide a switch-style dictionary to add assignments."""
        self.add = {
            Assignment.READING:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.add_new_reading(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    readings=reading_list,
                    status=state)
            ),
            Assignment.HOMEWORK:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.add_new_homework(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    problems=problems,
                    status=state)
            ),
            Assignment.EXTERNAL:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.add_new_external(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    assignment_url=url,
                    status=state)
            ),
            Assignment.EVENT:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.add_new_event(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    status=state)
            ),
        }
        self.edit = {
            Assignment.READING:
            (
                lambda driver, name, feedback, description='', periods={},
                reading_list={}, state=Assignment.DRAFT, problems=None, url='':
                self.change_reading(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    readings=reading_list,
                    status=state)
            ),
            Assignment.HOMEWORK:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.change_homework(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    problems=problems,
                    status=state)
            ),
            Assignment.EXTERNAL:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.change_external(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    assignment_url=url,
                    status=state)
            ),
            Assignment.EVENT:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.change_event(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    status=state)
            ),
        }
        self.remove = {
            Assignment.READING:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.delete_reading(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    readings=reading_list,
                    status=state)
            ),
            Assignment.HOMEWORK:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.delete_homework(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    problems=problems,
                    status=state,
                    feedback=feedback)
            ),
            Assignment.EXTERNAL:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.delete_external(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    assignment_url=url,
                    status=state)
            ),
            Assignment.EVENT:
            (
                lambda driver, name, description, periods, reading_list, state,
                problems, url, feedback:
                self.delete_event(
                    driver=driver,
                    title=name,
                    description=description,
                    periods=periods,
                    status=state)
            ),
        }

    @classmethod
    def rword(cls, length):
        """Return a <length>-character random string."""
        return ''.join(random.choice(string.ascii_lowercase)
                       for i in range(length))

    @classmethod
    def scroll_to(cls, driver, element):
        """Execute a scroll until in view javascript."""
        driver.execute_script('return arguments[0].scrollIntoView();', element)
        driver.execute_script('window.scrollBy(0, -80);')

    @classmethod
    def send_keys(cls, driver, element, text):
        """Send data to an element using javascript."""
        Assignment.scroll_to(driver, element)
        element.clear()
        time.sleep(0.5)
        for ch in text:
            element.send_keys(ch)

    def open_assignment_menu(self, driver):
        """Open the Add Assignment menu if it is closed."""
        try:
            assignment_menu = driver.find_element(
                By.XPATH, '//button[contains(@class,"dropdown-toggle")]')
            # if the Add Assignment menu is not open
            if 'open' not in assignment_menu.find_element(By.XPATH, '..'). \
                    get_attribute('class'):
                assignment_menu.click()
        except:
            return

    def assign_periods(self, driver, periods):
        """Assign open and close dates."""
        # assign the same dates for all periods
        today = datetime.date.today()
        if 'all' in periods:
            driver.find_element(By.ID, 'hide-periods-radio').click()
            opens_on, closes_on = periods['all']
            today = datetime.date.today()
            driver.find_element(
                By.XPATH, '//div[contains(@class,"-due-date")]' +
                '//div[contains(@class,"datepicker__input")]'
            ).click()
            # get calendar to correct month
            month = today.month
            year = today.year
            while (month != int(closes_on[:2]) or year != int(closes_on[6:])):
                driver.find_element(
                    By.XPATH,
                    '//a[contains(@class,"navigation--next")]'
                ).click()
                if month != 12:
                    month += 1
                else:
                    month = 1
                    year += 1
            driver.find_element(
                By.XPATH, '//div[contains(@class,"datepicker__day")' +
                'and contains(text(),"' + (closes_on[3:5]).lstrip('0') + '")]'
            ).click()
            time.sleep(0.5)
            driver.find_element(
                By.CLASS_NAME,
                'assign-to-label'
            ).click()
            driver.find_element(
                By.XPATH, '//div[contains(@class,"-open-date")]' +
                '//div[contains(@class,"datepicker__input")]'
            ).click()
            # get calendar to correct month
            month = today.month
            year = today.year
            while (month != int(opens_on[:2]) or year != int(opens_on[6:])):
                driver.find_element(
                    By.XPATH,
                    '//a[contains(@class,"navigation--next")]'
                ).click()
                if month != 12:
                    month += 1
                else:
                    month = 1
                    year += 1
            driver.find_element(
                By.XPATH, '//div[contains(@class,"datepicker__day")' +
                'and contains(text(),"' + (opens_on[3:5]).lstrip('0') + '")]'
            ).click()
            time.sleep(0.5)
            driver.find_element(
                By.CLASS_NAME,
                'assign-to-label'
            ).click()
            return
        # or set the dates for each period: {period: (open, close)}
        count = 0
        last = len(periods)
        for period in periods:
            count += 1
            if count > last:
                break
                if periods[period] is 'all' or period is 'skip':
                    continue
                opens_on, closes_on = periods[period]
                driver.find_element(
                    By.XPATH,
                    '//input[@id="period-toggle-%s"]' % count +
                    '/../following-sibling::div/following-sibling::div' +
                    '//input[contains(@class,"picker")]'
                ).send_keys(closes_on)
                time.sleep(0.5)
                driver.find_element(By.CLASS_NAME, 'assign-to-label').click()
                driver.find_element(
                    By.XPATH,
                    '//input[@id="period-toggle-%s"]' % count +
                    '/../following-sibling::div' +
                    '//input[contains(@class,"picker")]'
                ).send_keys(opens_on)
                time.sleep(0.5)
                driver.find_element(By.CLASS_NAME, 'assign-to-label').click()

    def select_status(self, driver, status):
        """Select assignment status."""
        if status == self.PUBLISH:
            print('Publishing...')
            element = driver.find_element(By.CLASS_NAME, 'footer-buttons')
            Assignment.scroll_to(driver, element)
            time.sleep(1)
            driver.find_element(
                By.XPATH, '//button[contains(@class,"-publish")]').click()
        elif status == self.DRAFT:
            print('Saving draft')
            element = driver.find_element(By.CLASS_NAME, 'footer-buttons')
            Assignment.scroll_to(driver, element)
            time.sleep(1)
            element = driver.find_element(
                By.XPATH, '//button[contains(@class," -save")]').click()
        elif status == self.CANCEL:
            print('Canceling assignment')
            element = driver.find_element(By.CLASS_NAME, 'footer-buttons')
            Assignment.scroll_to(driver, element)
            time.sleep(1)
            element = driver.find_element(
                By.XPATH,
                '//button[contains(@aria-role,"close") and @type="button"]'
            ).click()
            try:
                wait = WebDriverWait(driver, Assignment.WAIT_TIME)
                wait.until(
                    expect.visibility_of_element_located(
                        (By.XPATH, '//button[contains(@class,"ok")]')
                    )
                ).click()
            except:
                pass
        elif status == self.DELETE:
            print('Deleting assignment')
            element = driver.find_element(By.CLASS_NAME, 'footer-buttons')
            Assignment.scroll_to(driver, element)
            time.sleep(1)
            element = driver.find_element(
                By.XPATH,
                '//span[contains(text(),"Delete")]/..'
            ).click()
            wait = WebDriverWait(driver, Assignment.WAIT_TIME)
            wait.until(
                expect.visibility_of_element_located(
                    (By.XPATH, '//button[contains(@class,"ok")]')
                )
            ).click()

    def open_chapter_list(self, driver, chapter):
        """Open the reading chapter list."""
        data_chapter = driver.find_element(
            By.XPATH,
            '//h2[contains(@data-chapter-section,"%s")]/a' % chapter
        )
        if (data_chapter.get_attribute('aria-expanded')) == 'false':
            data_chapter.click()

    def select_sections(self, driver, chapters):
        """Select the sections and chapters."""
        for section in chapters:
            if 'ch' in section:  # select the whole chapter
                print('Adding chapter: ' + section)
                chapter = driver.find_element(
                    By.XPATH,
                    '//h2[@data-chapter-section="%s"]' % section[2:] +
                    '//i[contains(@class,"tutor-icon")]'
                )
                time.sleep(0.5)
                if not chapter.is_selected():
                    chapter.click()
            elif 'tutor' in section:
                continue
            else:  # select an individual section
                print('Adding section: ' + section)
                self.open_chapter_list(driver, section.split('.')[0])
                time.sleep(0.5)
                wait = WebDriverWait(driver, Assignment.WAIT_TIME)
                marked = wait.until(
                    expect.visibility_of_element_located(
                        (By.XPATH,
                         ('//span[contains(@data-chapter-section' +
                          ',"{s}") and text()="{s}"]').format(s=section) +
                         '/preceding-sibling::span/input')
                    )
                )
                if not marked.is_selected():
                    marked.click()

    def add_new_reading(self, driver, title, description, periods, readings,
                        status, break_point=None):
        """Add a new reading assignment.

        driver:      WebDriver - Selenium WebDriver instance
        title:       string    - assignment title
        description: string    - assignment description or additional
                                 instructions
        periods:     dict      - <key>:   string <period name> OR 'all'
                                 <value>: tuple  (<open date>, <close date>)
                                          date format is 'MM/DD/YYYY'
        readings:    [string]  - chapter and section numbers to include in the
                                 assignment; chapter numbers are prefixed with
                                 'ch'
        status:      string    - 'publish', 'cancel', or 'draft'
        """
        print('Creating a new Reading')
        self.open_assignment_menu(driver)
        driver.find_element(By.LINK_TEXT, 'Add Reading').click()
        time.sleep(1)
        wait = WebDriverWait(driver, Assignment.WAIT_TIME * 3)
        wait.until(
            expect.element_to_be_clickable(
                (By.ID, 'reading-title')
            )
        )
        if break_point == Assignment.BEFORE_TITLE:
            return
        driver.find_element(By.ID, 'reading-title').send_keys(title)
        if break_point == Assignment.BEFORE_DESCRIPTION:
            return
        driver.find_element(
            By.XPATH,
            '//div[contains(@class,"assignment-description")]//textarea' +
            '[contains(@class,"form-control")]'). \
            send_keys(description)
        if break_point == Assignment.BEFORE_PERIOD:
            return
        self.assign_periods(driver, periods)
        # add reading sections to the assignment
        driver.find_element(By.ID, 'reading-select').click()
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//div[contains(@class,"reading-plan")]')
            )
        )
        if break_point == Assignment.BEFORE_SECTION_SELECT:
            return
        self.select_sections(driver, readings)
        if break_point == Assignment.BEFORE_READING_SELECT:
            return
        driver.find_element(By.XPATH,
                            '//button[text()="Add Readings"]').click()
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//span[text()="Publish"]')
            )
        )
        if break_point == Assignment.BEFORE_STATUS_SELECT:
            return
        self.select_status(driver, status)

    def find_all_questions(self, driver, problems):
        """Final all available questions."""
        questions = {}
        section = ''
        wait = WebDriverWait(driver, 5)
        try:
            loading = wait.until(
                expect.visibility_of_element_located(
                    (By.XPATH, '//span[text()="Loading..."]')
                )
            )
            wait.until(expect.staleness_of(loading))
        except:
            pass
        rows = driver.find_elements(
            By.XPATH,
            '//div[contains(@class,"add-exercise-list")]/*[@class="row"]')
        for row in rows:
            children = row.find_elements(By.XPATH, './*')
            if len(children) == 0:
                # print('FAQ - No children tags')
                continue
            elif len(children) == 1:
                try:
                    section = children[0].find_element(
                        By.XPATH,
                        './/span[@class="chapter-section"]').text
                    questions[section] = []
                except:
                    question = children[0].find_element(
                        By.XPATH,
                        './/span[contains(text(),"@")]').text
                    question = question.split(' ')[1]
                    questions[section].append(question)
            else:
                question = children[0].find_element(
                    By.XPATH,
                    './/span[contains(text(),"@")]').text
                question = question.split(' ')[1]
                questions[section].append(question)
                try:
                    question = children[1].find_element(
                        By.XPATH,
                        './/span[contains(text(),"@")]').text
                    question = question.split(' ')[1]
                    questions[section].append(question)
                except:
                    pass
        return questions

    def get_chapter_list(self, problems, chapter_id):
        """Return available chapters."""
        available = []
        chapter = int(chapter_id[2:])
        for section in problems:
            if int(section.split('.')[0]) == chapter:
                for i in range(len(problems[section])):
                    available.append(problems[section][i])
        return available

    def set_tutor_selections(self, driver, problems):
        """Select the number of Tutor selected problems."""
        tutor_picks = driver.find_element(
            By.XPATH, '//div[@class="tutor-selections"]//h2')
        current = int(tutor_picks.text)
        change = int(problems['tutor']) - current
        if change != 0:
            increase = driver.find_element(
                By.XPATH,
                '//div[@class="tutor-selections"]' +
                '//button[contains(@class,"-move-exercise-down")]'
            )
            decrease = driver.find_element(
                By.XPATH,
                '//div[@class="tutor-selections"]' +
                '//button[contains(@class,"-move-exercise-up")]'
            )
            while change < 0:
                change += 1
                increase.click()
            while change > 0:
                change -= 1
                decrease.click()

    def add_homework_problems(self, driver, problems):
        """Add assessments to a homework."""
        wait = WebDriverWait(driver, Assignment.WAIT_TIME)
        driver.find_element(By.ID, 'problems-select').click()
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//span[text()="Add Problems"]')
            )
        )
        self.select_sections(driver, list(problems.keys()))
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.find_element(
            By.XPATH, '//button[contains(@class,"-show-problems")]'
        ).click()
        all_available = self.find_all_questions(driver, problems)
        using = []
        # print('AHP - Selection list: %s' % selections)
        for section in problems:
            if problems is None or str(problems).lower() == 'none':
                print('%s: No exercises (%s)' % (section, problems[section]))
                continue
            # Set maximum Tutor-selected problems
            if section == 'tutor':
                print('Using %s Tutor selections' % problems[section])
                self.set_tutor_selections(driver, problems)
            # Select all exercises in the section
            elif problems[section] == 'all':
                print('Selecting all from %s' % section)
                available = self.get_chapter_list(all_available, section) if \
                    'ch' in section else all_available[section]
                for ex in available:
                    using.append(ex)
            # Select between X and Y exercises, inclusive, from the section
            elif type(problems[section]) == tuple:
                low, high = problems[section]
                total = random.randint(int(low), int(high))
                print('Selecting %s random from %s (%s to %s)' %
                      (total, section, low, high))
                available = self.get_chapter_list(all_available, section) if \
                    'ch' in section else all_available[section]
                for i in range(total):
                    ex = random.randint(0, len(available) - 1)
                    using.append(available[ex])
                    available.remove(available[ex])
            # Select the first X exercises from the section
            elif type(problems[section]) == int:
                print('Selecting first %s from %s' %
                      (problems[section], section))
                available = self.get_chapter_list(all_available, section) if \
                    'ch' in section else all_available[section]
                for position in range(problems[section]):
                    using.append(available[position])
            elif problems[section] is list:
                print('Adding %s custom if available' % len(problems[section]))
                for ex in problems[section]:
                    for section in all_available:
                        if ex in all_available[section]:
                            using.append(ex)
        for exercise in set(using):
            ac = ActionChains(driver)
            time.sleep(0.5)
            ac.move_to_element(
                driver.find_element(
                    By.XPATH,
                    '//span[contains(@data-reactid,"%s")]' % exercise
                )
            )
            ac.move_by_offset(0, -80)
            ac.click()
            ac.perform()
        ActionChains(driver). \
            move_to_element(
                driver.find_element(
                    By.XPATH, '//span[text()="Tutor Selections"]'
                )). \
            move_by_offset(0, -80). \
            perform()
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//*[text()="Next"]')
            )
        ).click()

    def add_new_homework(self, driver, title, description, periods, problems,
                         status, feedback, break_point=None):
        """Add a new homework assignment.

        driver:      WebDriver - Selenium WebDriver instance
        title:       string    - assignment title
        description: string    - assignment description or additional
                                 instructions
        periods:     dict      - <key>:   string <period name> OR 'all'
                                 <value>: tuple  (<open date>, <close date>)
                                          date format is 'MM/DD/YYYY'
        problems:    dict      - <key>:   string '<chapter.section>' or 'tutor'
                               - <value>: [string] Ex-IDs
                                          int use first <int> exercises
                                              available
                                          (int, int) between <min> and <max>
                                              exercises
                                          'all' select all exercises in a
                                              section
                                          int 'tutor' takes 2, 3, or 4
                                              default: 3
        status:      string    - 'publish', 'cancel', or 'draft'
        feedback:    string    - 'immediate', 'non-immediate'
        """
        print('Creating a new Homework')
        self.open_assignment_menu(driver)
        driver.find_element(By.LINK_TEXT, 'Add Homework').click()
        wait = WebDriverWait(driver, Assignment.WAIT_TIME)
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//div[contains(@class,"homework-plan")]')
            )
        )
        if break_point == Assignment.BEFORE_TITLE:
            return
        driver.find_element(By.ID, 'reading-title').send_keys(title)
        if break_point == Assignment.BEFORE_DESCRIPTION:
            return
        driver.find_element(
            By.XPATH,
            '//div[contains(@class,"assignment-description")]' +
            '//textarea[contains(@class,"form-control")]'). \
            send_keys(description)
        if break_point == Assignment.BEFORE_PERIOD:
            return
        self.assign_periods(driver, periods)
        if break_point == Assignment.BEFORE_EXERCISE_SELECT:
            return
        self.add_homework_problems(driver, problems)
        driver.find_element(By.ID, 'feedback-select').click()
        if feedback == 'immediate':
            driver.find_element(
                By.XPATH,
                '//option[@value="immediate"]'
            ).click()
        else:
            driver.find_element(By.XPATH, '//option[@value="due_at"]').click()
        if break_point == Assignment.BEFORE_STATUS_SELECT:
            return
        self.select_status(driver, status)

    def add_new_external(self, driver, title, description, periods,
                         assignment_url, status, break_point=None):
        """Add a new external assignment.

        driver:      WebDriver - Selenium WebDriver instance
        title:       string    - assignment title
        description: string    - assignment description or additional
                                 instructions
        periods:     dict      - <key>:   string <period name> OR 'all'
                                 <value>: tuple  (<open date>, <close date>)
                                          date format is 'MM/DD/YYYY'
        assignment_url:    string      - website name
        status:      string    - 'publish', 'cancel', or 'draft'
        """
        print('Creating a new External Assignment')
        self.open_assignment_menu(driver)
        driver.find_element(By.LINK_TEXT, 'Add External Assignment').click()
        time.sleep(1)
        wait = WebDriverWait(driver, Assignment.WAIT_TIME * 3)
        wait.until(
            expect.element_to_be_clickable(
                (By.ID, 'reading-title')
            )
        )
        if break_point == Assignment.BEFORE_TITLE:
            return
        driver.find_element(By.ID, 'reading-title').send_keys(title)
        if break_point == Assignment.BEFORE_DESCRIPTION:
            return
        driver.find_element(
            By.XPATH,
            '//div[contains(@class,"assignment-description")]//textarea' +
            '[contains(@class,"form-control")]'). \
            send_keys(description)
        if break_point == Assignment.BEFORE_PERIOD:
            return
        self.assign_periods(driver, periods)
        if break_point == Assignment.BEFORE_URL:
            return
        driver.find_element(By.ID, 'external-url').send_keys(assignment_url)
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//span[text()="Publish"]')
            )
        )
        if break_point == Assignment.BEFORE_STATUS_SELECT:
            return
        self.select_status(driver, status)

    def add_new_event(self, driver, title, description, periods, status,
                      break_point=None):
        """Add a new external assignment.

        driver:      WebDriver - Selenium WebDriver instance
        title:       string    - assignment title
        description: string    - assignment description or additional
                                 instructions
        periods:     dict      - <key>:   string <period name> OR 'all'
                                 <value>: tuple  (<open date>, <close date>)
                                          date format is 'MM/DD/YYYY'
        status:      string    - 'publish', 'cancel', or 'draft'
        """
        print('Creating a new Event')
        self.open_assignment_menu(driver)
        driver.find_element(By.LINK_TEXT, 'Add Event').click()
        time.sleep(1)
        wait = WebDriverWait(driver, Assignment.WAIT_TIME * 3)
        wait.until(
            expect.element_to_be_clickable(
                (By.ID, 'reading-title')
            )
        )
        if break_point == Assignment.BEFORE_TITLE:
            return
        driver.find_element(By.ID, 'reading-title').send_keys(title)
        if break_point == Assignment.BEFORE_DESCRIPTION:
            return
        driver.find_element(
            By.XPATH,
            '//div[contains(@class,"assignment-description")]//textarea' +
            '[contains(@class,"form-control")]'). \
            send_keys(description)
        if break_point == Assignment.BEFORE_PERIOD:
            return
        self.assign_periods(driver, periods)
        wait.until(
            expect.visibility_of_element_located(
                (By.XPATH, '//span[text()="Publish"]')
            )
        )
        if break_point == Assignment.BEFORE_STATUS_SELECT:
            return
        self.select_status(driver, status)

    def add_new_review(self, driver, title, description, periods, assessments,
                       assignment_url, status):
        """Add a review assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def change_reading(self, driver, title, description='', periods={},
                       readings=[], status=DRAFT):
        """Edit a reading assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def change_homework(self, driver, title, description, periods, problems,
                        status):
        """Edit a homework assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def change_external(self, driver, title, description, periods,
                        assignment_url, status):
        """Edit an external assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def change_event(self, driver, title, description, periods, status):
        """Edit an event."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def delete_reading(self, driver, title, description, periods, readings,
                       status):
        """Delete a reading assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def delete_homework(self, driver, title, description, periods, problems,
                        status):
        """Delete a homework assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def delete_external(self, driver, title, description, periods,
                        assignment_url, status):
        """Delete an external assignment."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

    def delete_event(self, driver, title, description, periods, status):
        """Delete an event."""
        raise NotImplementedError(inspect.currentframe().f_code.co_name)
