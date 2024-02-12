import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class SpellcheckingService {

  private apiUrl: string = 'http://localhost:5000/api/spellcheck-nlp'

  constructor(private httpClient: HttpClient) { }

  spellcheckSingleWord(inputWord: string): Observable<any> {
    return this.httpClient.post(this.apiUrl, { query: inputWord });
  }
}
