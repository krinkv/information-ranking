import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Article} from "../dto/article";

@Injectable({
  providedIn: 'root'
})
export class DocumentRetrievingService {
  private apiSearchUrl: string = 'http://localhost:5000/api/search'
  private apiDocumentUrl: string = 'http://localhost:5000/api/documents/'

  constructor(private httpClient: HttpClient) { }

  getBestDocumentCandidates(inputQuery: string): Observable<any> {
    return this.httpClient.post(this.apiSearchUrl, { query: inputQuery });
  }

  getSingleDocument(docId: string): Observable<any> {
    return this.httpClient.get(this.apiDocumentUrl + docId);
  }
}
