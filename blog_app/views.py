from django.shortcuts import render

# Create your views here.
import mysql.connector
from mysql.connector import Error
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Database connection
def index(request):
    return render(request, 'blog_app/index.html')
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='729666',
            database='4153hw1_blog'
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        exit(1)

# Create a blog post
@csrf_exempt
def create_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        writer_uni = data.get('writer_uni')
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "INSERT INTO blog (tittle, content, writter_uni) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, content, writer_uni))
            conn.commit()
            return JsonResponse({'message': 'Blog created successfully!'})
        except Error as e:
            return JsonResponse({'error': f'Create blog failed: {e}'})
        finally:
            conn.close()

# Edit a blog post
@csrf_exempt
def edit_blog(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        blog_number = data.get('blog_number')
        new_title = data.get('new_title')
        new_content = data.get('new_content')
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "UPDATE blog SET tittle=%s, content=%s WHERE blog_number=%s"
            cursor.execute(query, (new_title, new_content, blog_number))
            conn.commit()
            return JsonResponse({'message': 'Blog updated successfully!'})
        except Error as e:
            return JsonResponse({'error': f'Edit blog failed: {e}'})
        finally:
            conn.close()

# Delete a blog post
@csrf_exempt
def delete_blog(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        blog_number = data.get('blog_number')
        student_uni = data.get('student_uni')
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "DELETE FROM blog WHERE id=%s AND student_uni=%s"
            cursor.execute(query, (blog_number, student_uni))
            conn.commit()
            return JsonResponse({'message': 'Blog deleted successfully!'})
        except Error as e:
            return JsonResponse({'error': f'Delete blog failed: {e}'})
        finally:
            conn.close()

# Reply to a blog post
@csrf_exempt
def reply_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        writer_uni = data.get('writer_uni')
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "INSERT INTO comment (content, writter_uni) VALUES (%s, %s)"
            cursor.execute(query, (content, writer_uni))
            conn.commit()
            return JsonResponse({'message': 'Reply added successfully!'})
        except Error as e:
            return JsonResponse({'error': f'Reply failed: {e}'})
        finally:
            conn.close()

# Query blogs by priority
@csrf_exempt
def query_blog_by_priority(request):
    if request.method == 'GET':
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT tittle, content, writter_uni FROM blog ORDER BY priority DESC"
            cursor.execute(query)
            result = cursor.fetchall()
            if not result:
                return JsonResponse({'message': 'No results found.'})
            else:
                blogs = [{'title': row[0], 'content': row[1], 'writer_uni': row[2]} for row in result]
                return JsonResponse({'blogs': blogs})
        except Error as e:
            return JsonResponse({'error': f'Query failed: {e}'})
        finally:
            conn.close()

# Search blog by keyword
@csrf_exempt
def search_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        keyword = data.get('keyword')
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT tittle, content, writter_uni FROM blog WHERE tittle LIKE %s"
            cursor.execute(query, (f"%{keyword}%",))
            result = cursor.fetchall()
            if not result:
                return JsonResponse({'message': 'No matching results.'})
            else:
                blogs = [{'title': row[0], 'content': row[1], 'writer_uni': row[2]} for row in result]
                return JsonResponse({'blogs': blogs})
        except Error as e:
            return JsonResponse({'error': f'Search failed: {e}'})
        finally:
            conn.close()
